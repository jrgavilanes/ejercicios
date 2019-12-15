from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
db = SQLAlchemy(app)


class Tarea(db.Model):
    __tablename__ = "tareas"
    id = db.Column(db.Integer, primary_key=True)
    tarea = db.Column(db.String(200))
    done = db.Column(db.Boolean, default=False)


@app.route("/")
def home():
    tareas = Tarea.query.all()
    return render_template("index.html", tareas=tareas)


@app.route("/create-task", methods=["POST"])
def create():
    tarea = Tarea(tarea=request.form.get("tarea"))
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/edit-task/<id>")
def update(id):
    tarea = Tarea.query.filter_by(id=int(id)).first()
    tarea.done = not(tarea.done)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete-task/<id>")
def delete(id):
    Tarea.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
