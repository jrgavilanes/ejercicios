import os
import secrets
import bcrypt
import requests

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

GOODREADS_APIKEY = "ixvt0qDECZIn3AXpETLR2g"

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine("sqlite:///database/db.sqlite")
db = scoped_session(sessionmaker(bind=engine))

active_sessions = {}

@app.route("/")
def home():

    if get_user_id() is None:
        return redirect(url_for("login"))

    return redirect(url_for("main"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":

        if get_user_id() is None:
            return render_template("login.html")

        return redirect(url_for("main"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.execute(" SELECT * FROM usuarios WHERE email = :email",
                          {"email": email}).fetchone()

        if user is None:
            # return redirect(url_for("login"))
            error_message = "Usuario no válido"
            return render_template("login.html", error_message=error_message)

        if user["email"] == email and bcrypt.checkpw(password.encode(), user["password"].encode()):
            token = secrets.token_urlsafe(16)
            session["session-token"] = token
            session["user-email"] = email
            # db.execute("update usuarios set active_session= :active_session where id = :id", {
            #            "active_session": token,
            #            "id": user["id"]})
            # db.commit()
            active_sessions[token] = user["id"]
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        if get_user_id() is None:
            return render_template("register.html")

        return redirect(url_for("main"))

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        token = secrets.token_urlsafe(16)

        db.execute("INSERT INTO usuarios (email,password,active_session) VALUES(:email, :password, :active_session)", {
            "email": email,
            "password": password,
            "active_session": token
        })

        db.commit()

        user = db.execute(" SELECT id FROM usuarios WHERE email = :email",
                          {"email": email}).fetchone()

        if not user is None:
            session["session-token"] = token
            session["user-email"] = email
            active_sessions[token] = user["id"]
            return redirect(url_for("home"))
        else:
            return redirect(url_for("register"))


@app.route("/logout")
def logout():
    try:
        del active_sessions[session["session-token"]]
    except KeyError:
        pass

    return redirect(url_for("login"))


@app.route("/main", methods=["GET", "POST"])
def main():

    if get_user_id() is None:
        return redirect(url_for("login"))

    user_email = session["user-email"]
    filtro = ""

    if request.method == "GET":
        libros = db.execute("SELECT * FROM libros LIMIT 20").fetchall()

    if request.method == "POST":
        filtro = request.form.get("query")
        filtro = "%"+filtro+"%"

        libros = db.execute("SELECT * FROM libros WHERE isbn LIKE :query OR titulo LIKE :query OR autor LIKE :query", {
            "query": filtro
        }).fetchall()

        filtro = filtro[1:-1]

    return render_template("index.html", libros=libros, user_email=user_email, filtro=filtro)


@app.route("/book/<isbn>")
def book(isbn):

    if get_user_id() is None:
        return redirect(url_for("login"))

    user_email = session["user-email"]

    libro = db.execute(
        "SELECT * FROM libros where isbn = :isbn", {"isbn": isbn}).fetchone()
    comentarios = db.execute(
        "SELECT * FROM comentarios, usuarios where usuarios.id=comentarios.id_usuario and isbn = :isbn", {"isbn": isbn}).fetchall()

    g_reads = {}
    g_reads["average_rating"] = ""
    g_reads["ratings_count"] = ""

    try:
        goodreads = requests.get("https://www.goodreads.com/book/review_counts.json", params={
            "key": GOODREADS_APIKEY,
            "isbns": isbn}).json()
        g_reads["average_rating"] = goodreads['books'][0]["average_rating"]
        g_reads["ratings_count"] = goodreads['books'][0]["ratings_count"]
    except:
        pass

    return render_template("book_detail.html", libro=libro, user_email=user_email, comentarios=comentarios, goodreads=g_reads)


@app.route("/book/comment", methods=['POST'])
def insert_comment():

    if get_user_id() is None:
        return redirect(url_for("login"))

    user_email = session["user-email"]

    print("Llega:", get_user_id(), request.form.get("isbn"),
          request.form.get("comentario"), request.form.get("puntuacion"))

    try:
        db.execute("INSERT INTO `comentarios` (id_usuario, isbn, comentario, puntuacion) VALUES (:id_usuario, :isbn, :comentario, :puntuacion)", {
            "id_usuario": get_user_id(),
            "isbn": request.form.get("isbn"),
            "comentario": request.form.get("comentario"),
            "puntuacion": request.form.get("puntuacion")})

        db.commit()
    except:
        pass

    return redirect(url_for('book', isbn=request.form.get("isbn")))



@app.route("/api/<isbn>")
def api(isbn):

    # if get_user_id() is None:
    #     return redirect(url_for("login"))

    result = {}

    libro = db.execute(
        "SELECT isbn, titulo, autor, anyo FROM libros where isbn = :isbn", {"isbn": isbn}).fetchone()

    if libro is None:
        return jsonify(error=404, text="Libro no encontrado"), 404


    result["isbn"], result["titulo"], result["autor"], result["año"] = libro

        
    suma, result["num_comentarios"] = db.execute(
        "SELECT SUM(PUNTUACION) suma, COUNT(isbn) num_comentarios FROM comentarios WHERE isbn = :isbn;", {"isbn": isbn}).fetchone()

     
    if result["num_comentarios"] == 0:
        result["puntuacion_media"] = "N/A"
    else:
        result["puntuacion_media"] = suma/result["num_comentarios"]

    return jsonify(result)


def get_user_id():

    if session.get("session-token") is None:
        return None

    return active_sessions.get(session.get("session-token"), None)


if __name__ == "__main__":
    app.run(debug=True)
