import os

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
    if session.get("user_id") is None:
        return redirect(url_for("login"))

    else:
        return redirect(url_for("main"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        html_login="""
            <form action="/login" method="POST">
                <input type="text" name="email" id="email" placeholder="email" autofocus>
                <input type="password" name="password" id="password" placeholder="password">
                <button type="submit">Acceder</button>
            </form>
        """
        return html_login


    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.execute(" SELECT * FROM usuarios WHERE email = :email AND password = :password",
                          {"email": email, "password": password}).fetchone()

        if user is None:
            return redirect(url_for("login"))

        if user["email"] == email and user["password"] == password:
            session["user_id"] = user["id"]
            session["active_session"] = "bla bla bla"
            db.execute("update usuarios set active_session= :active_session", {
                       "active_session": "bla bla bla"})
            db.commit()
            active_sessions[user["id"]] = "bla bla bla"
            return redirect(url_for("home"))
        else:
            return redirect(url_for("login"))


@app.route("/registrar", methods=["GET", "POST"])
def register():
    pass


@app.route("/main", methods=["GET", "POST"])
def main():
    if session.get("user_id") is None:
        return redirect(url_for("login"))

    if session.get("active_session") != active_sessions[session.get("user_id")]:
        return redirect(url_for("login"))

    return "cositas wapas de mi sesión"



if __name__ == "__main__":
    app.run(debug=True)
