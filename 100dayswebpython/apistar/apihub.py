import json
import os
import shutil


# Configuracion
PATH_APP = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = os.path.join(PATH_APP, "config.json")

config = {}


def load_config(filename: str):
    """Carga configuración"""
    try:
        with open(filename) as f:
            config = f.read()
            config = json.loads(config)
            return config

    except FileNotFoundError as e:
        raise Exception("Error", e)


def save_config(config: dict, filename: str):
    """ Salva configuracion """
    try:
        with open(filename, "w") as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
    except Exception as e:
        raise Exception("Error", e)


config = load_config(CONFIG_FILE)


if not os.path.exists(os.path.join(PATH_APP, "datos")):
    os.makedirs(os.path.join(PATH_APP, "datos"))

if not os.path.exists(os.path.join(PATH_APP, "datos", "entrada")):
    os.makedirs(os.path.join(PATH_APP, "datos", "entrada"))

if not os.path.exists(os.path.join(PATH_APP, "datos", "salida")):
    os.makedirs(os.path.join(PATH_APP, "datos", "salida"))

if not os.path.exists(os.path.join(PATH_APP, "datos", "historico")):
    os.makedirs(os.path.join(PATH_APP, "datos", "historico"))

if not os.path.exists(os.path.join(PATH_APP, "datos", "aplicaciones")):
    os.makedirs(os.path.join(PATH_APP, "datos", "aplicaciones"))

for app in config["aplicaciones"]:

    if not os.path.exists(os.path.join(PATH_APP, "datos", "aplicaciones", app)):
        os.makedirs(os.path.join(PATH_APP, "datos", "aplicaciones", app))

    if not os.path.exists(os.path.join(PATH_APP, "datos", "aplicaciones", app, "entrada")):
        os.makedirs(os.path.join(PATH_APP, "datos",
                                 "aplicaciones", app, "entrada"))

    if not os.path.exists(os.path.join(PATH_APP, "datos", "aplicaciones", app, "historico")):
        os.makedirs(os.path.join(PATH_APP, "datos",
                                 "aplicaciones", app, "historico"))

    if not os.path.exists(os.path.join(PATH_APP, "datos", "aplicaciones", app, "salida")):
        os.makedirs(os.path.join(PATH_APP, "datos",
                                 "aplicaciones", app, "salida"))

    if config["aplicaciones"][app]['bloqueado']:
        if not os.path.exists(os.path.join(PATH_APP, "datos", "aplicaciones", app, "salida", "BLOQUEADO")):
            os.mknod(os.path.join(PATH_APP, "datos",
                                  "aplicaciones", app, "salida", "BLOQUEADO"))
    else:
        if os.path.exists(os.path.join(PATH_APP, "datos", "aplicaciones", app, "salida", "BLOQUEADO")):
            os.remove(os.path.join(PATH_APP, "datos",
                                   "aplicaciones", app, "salida", "BLOQUEADO"))


for remove_dir in os.listdir(os.path.join(PATH_APP, "datos", "aplicaciones")):
    if remove_dir not in config["aplicaciones"]:
        shutil.rmtree(os.path.join(PATH_APP, "datos",
                                   "aplicaciones", remove_dir), ignore_errors=True)

# print(os.listdir(os.path.join(PATH_APP, "datos", "aplicaciones")))

# save_config(config, CONFIG_FILE)
