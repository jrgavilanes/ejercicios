# Apuntes FLASK

## Estructura proyecto

```
mkdir MI_PROYECTO && cd MI_PROYECTO
mkdir app
mkdir app/templates
mkdir app/static
mkdir app/static/js
mkdir app/static/css
mkdir app/static/img
mkdir app/views
mkdir app/viewmodels
mkdir app/data
mkdir app/tests
touch app/app.py
touch app/requirements.txt
touch app/requirements-dev.txt


cat > app/app.py <<- EOM
import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return("hola nano!")

app.run()
EOM

cat > app/requirements.txt <<- EOM
flask
sqlalchemy
passlib
EOM

cat > app/requirements-dev.txt <<- EOM
-r requirements.txt
pytest
pytest-cov
webtest
EOM

```

### Instalar entorno virtual
Instalar
```
:~ MI_PROYECTO$ python3 -m venv venv
```
Activar
```
# Windows
:~ MI_PROYECTO$ . venv/Scripts/activate

# Linux
:~ MI_PROYECTO$ . venv/bin/activate
```

### Estructura obtenida

```
:~/MI_PROYECTO$ ls
app  venv
:~/MI_PROYECTO$ tree -I venv
.
└── app
    ├── app.py
    ├── data
    ├── requirements-dev.txt
    ├── requirements.txt
    ├── static
    │   ├── css
    │   ├── img
    │   └── js
    ├── templates
    ├── tests
    ├── viewmodels
    └── views

10 directories, 3 files
```

### Iniciar aplicación

```
(venv):~/MI_PROYECTO/app$ python app.py 
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### PIP: Uso básico

Ver paquetes instalados en el entorno
```
(venv):~/MI_PROYECTO$ pip list
pip (9.0.1)
pkg-resources (0.0.0)
setuptools (39.0.1)
```

Instalar paquetes desde requirements.txt
```
(venv):~/Code/flask_base/MI_PROYECTO/app$ pip install -r requirements.txt 
```

Guardar paquetes instalados en requirements.txt
```
(venv):~/Code/flask_base/MI_PROYECTO/app$ pip freeze > requirements.txt
```
