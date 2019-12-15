from flask import Flask, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

html_template="""
<form action="/" method="POST">
    <input type="text" name="tarea" id="tarea" placeholder="di algo" autofocus>
</form>
{x}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []

    
    if request.method == "POST":
        note = request.form.get("tarea")
        session["notes"].append(note)

    mi_respuesta = str(session["notes"])

    return html_template.replace("{x}", mi_respuesta)

if __name__ == "__main__":
    app.run(debug=True)


    