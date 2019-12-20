import os
import secrets
import bcrypt

from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine("sqlite:///db.sqlite")
db = scoped_session(sessionmaker(bind=engine))

active_sessions = {}

@app.route("/")
def home():

    if get_user_id() == -1:
        return redirect(url_for("login"))

    return redirect(url_for("main"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if get_user_id() != -1:
        return redirect(url_for("main"))

    if request.method == "GET":
        html_login = """
            <form action="/login" method="POST">
                <input type="text" name="email" id="email" placeholder="email" autofocus>
                <input type="password" name="password" id="password" placeholder="password">
                <button type="submit">Acceder</button>
            </form>
            <a href="/register">No tienes cuenta? Creáte una ya !</a>
        """
        return html_login

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.execute(" SELECT * FROM usuarios WHERE email = :email",{"email": email}).fetchone()

        if user is None:
            return redirect(url_for("login"))

        if user["email"] == email and bcrypt.checkpw(password.encode(),user["password"].encode()):
            token = secrets.token_urlsafe(16)
            session["session-token"] = token
            db.execute("update usuarios set active_session= :active_session where id = :id", {
                       "active_session": token,
                       "id": user["id"]})
            db.commit()
            active_sessions[token] = user["id"]
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if get_user_id() != -1:
        return redirect(url_for("main"))

    if request.method == "GET":
        html_register = """
            <form action="/register" method="POST">
                <input type="email" name="email" id="email" placeholder="email" autofocus required>
                <input type="password" name="password" id="password" placeholder="password" required>
                <input type="password" name="password1" id="password1" placeholder="repite password" required>
                <button type="submit">Crear cuenta</button>
            </form>
        """
        return html_register

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()       
        token = secrets.token_urlsafe(16)

        try:
            db.execute("INSERT INTO usuarios (email,password,active_session) VALUES(:email, :password, :active_session)", {
                "email": email,
                "password": password,
                "active_session": token
            })

            db.commit()

            user = db.execute(" SELECT id FROM usuarios WHERE email = :email",{"email": email}).fetchone()
            if not user is None:
                session["session-token"] = token
                active_sessions[token] = user["id"]
                return redirect(url_for("home"))
            else:
                return redirect(url_for("register"))

        except Exception as e:
            print(str(e))

        return redirect(url_for("register"))


@app.route("/main", methods=["GET", "POST"])
def main():

    if get_user_id() == -1:
        return redirect(url_for("login"))

    return f"cositas wapas del usuario {id_usuario}<br><a href='/logout'>Salir</a>"

@app.route("/logout", methods=["GET"])
def logout():
    if get_user_id() != -1:
        del active_sessions[session.get("session-token")]
        session.clear()

        
    return redirect(url_for("main"))



def get_user_id():

    if session.get("session-token") is None:
        return -1

    return active_sessions.get(session.get("session-token"), -1)


if __name__ == "__main__":
    app.run(debug=True)
