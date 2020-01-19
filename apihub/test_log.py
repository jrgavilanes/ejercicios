import os

from log import Log

def test_escribe_log():

    _, fichero_log = Log.escribe_log("test_log", "test_escribe_log", "texto de prueba")

    assert os.path.exists(fichero_log)

    with open(fichero_log, "r") as f:
        contenido = f.read()

    assert "texto de prueba" in contenido

    os.remove(fichero_log)