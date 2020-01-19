import pdb

import os
import shutil

import json
from datetime import datetime

from log import Log


class SistemaFicheros:

    def __init__(self, PATH_APP: str):
        self.config = {}
        self.PATH_APP = PATH_APP
        self.CONFIG_FILE = os.path.join(self.PATH_APP, "configuracion.json")
        self.DATOS_ENTRADA = os.path.join(self.PATH_APP, "datos", "entrada")
        self.DATOS_HISTORICO = os.path.join(self.PATH_APP,
                                            "datos",
                                            "historico")

    def guardar_configuracion(self):
        """ Salva configuracion """
        try:
            with open(self.CONFIG_FILE, "w") as f:
                json.dump(self.config, f, ensure_ascii=False, indent=4)
                return True

        except Exception as e:
            raise Exception("Error", e)

    def enrutar_archivos(self):
        """ Copia los archivos desde datos/entrada a la 
        salida de la aplicación que lo espera"""

        enrutadores = self.config["enrutador"]["ficheros"]

        ficheros = os.listdir(self.DATOS_ENTRADA)

        # Solo quiero los ficheros "tf-%" y me quedo con su %
        ficheros = [f[3:] for f in ficheros if f.find('tf-') == 0]

        for f in ficheros:

            fichero_tf = os.path.join(self.DATOS_ENTRADA, "tf-{}".format(f))

            if os.path.isfile(os.path.join(self.DATOS_ENTRADA, f)):
                fichero_origen = os.path.join(self.DATOS_ENTRADA, f)
                
                for enrutador in enrutadores:
                    if f.find(enrutador) == 0:
                        destinos = self.config["enrutador"]["ficheros"][enrutador]["aplicaciones"]
                        for destino in destinos:
                            fichero_destino = os.path.join(
                                self.PATH_APP, "datos", "aplicaciones", destino, "salida", f)
                            try:
                                shutil.copyfile(fichero_origen,
                                                fichero_destino)
                                Log.escribe_log("sistema_ficheros",
                                                "enrutar_archivos",
                                                "copio {} en {}".format(fichero_origen, fichero_destino))
                            except Exception as e:
                                os.remove(fichero_tf)
                                Log.escribe_log("sistema_ficheros",
                                                "enrutar_archivos",
                                                f"intento {fichero_origen} en {fichero_destino}. {e}",
                                                "ERROR")
                        break

                ahora = datetime.now()
                fichero_historico = "{}_{}{:02d}{:02d}".format(
                    f, ahora.year, ahora.month, ahora.day)
                fichero_historico = os.path.join(
                    self.PATH_APP, "datos", "historico", fichero_historico)
                try:
                    os.remove(fichero_tf)
                    shutil.move(fichero_origen, fichero_historico)
                    os.system(f"gzip {fichero_historico} -f")
                    Log.escribe_log("sistema_ficheros",
                                    "enrutar_archivos",
                                    f"historifico {f}")
                except Exception as e:
                    Log.escribe_log("sistema_ficheros",
                                    "enrutar_archivos",
                                    f"intento historificar {f}: {e}",
                                    "ERROR")

            else:

                # Si hay tf-% que no corresponde con ningún %, elimina el tf-%
                Log.escribe_log("sistema_ficheros",
                                "enrutar_archivos",
                                f"encontrado {fichero_tf} sin correspondencia",
                                "WARNING")

                os.remove(fichero_tf)

    def cargar_configuracion(self):
        """Carga configuración"""
        try:
            with open(self.CONFIG_FILE) as f:
                self.config = f.read()
                self.config = json.loads(self.config)
                return self.config

        except FileNotFoundError as e:
            raise Exception("Error", e)

    def actualiza_estructura(self):

        if not os.path.exists(os.path.join(self.PATH_APP, "datos")):
            os.makedirs(os.path.join(self.PATH_APP, "datos"))

        if not os.path.exists(os.path.join(self.PATH_APP, "datos", "entrada")):
            os.makedirs(os.path.join(self.PATH_APP, "datos", "entrada"))

        if not os.path.exists(os.path.join(self.PATH_APP, "datos", "salida")):
            os.makedirs(os.path.join(self.PATH_APP, "datos", "salida"))

        if not os.path.exists(os.path.join(self.PATH_APP, "datos", "historico")):
            os.makedirs(os.path.join(self.PATH_APP, "datos", "historico"))

        if not os.path.exists(os.path.join(self.PATH_APP, "datos", "log")):
            os.makedirs(os.path.join(self.PATH_APP, "datos", "log"))

        if not os.path.exists(os.path.join(self.PATH_APP, "datos", "aplicaciones")):
            os.makedirs(os.path.join(self.PATH_APP, "datos", "aplicaciones"))

        for app in self.config["aplicaciones"]:

            if not os.path.exists(os.path.join(self.PATH_APP, "datos", "aplicaciones", app)):
                os.makedirs(os.path.join(
                    self.PATH_APP, "datos", "aplicaciones", app))

            if not os.path.exists(os.path.join(self.PATH_APP, "datos", "aplicaciones", app, "entrada")):
                os.makedirs(os.path.join(self.PATH_APP, "datos",
                                         "aplicaciones", app, "entrada"))

            if not os.path.exists(os.path.join(self.PATH_APP, "datos", "aplicaciones", app, "historico")):
                os.makedirs(os.path.join(self.PATH_APP, "datos",
                                         "aplicaciones", app, "historico"))

            if not os.path.exists(os.path.join(self.PATH_APP, "datos", "aplicaciones", app, "salida")):
                os.makedirs(os.path.join(self.PATH_APP, "datos",
                                         "aplicaciones", app, "salida"))

            if self.config["aplicaciones"][app]['activo']:
                if os.path.exists(os.path.join(self.PATH_APP, "datos", "aplicaciones", app, "salida", "BLOQUEADO")):
                    os.remove(os.path.join(self.PATH_APP, "datos",
                                           "aplicaciones", app, "salida", "BLOQUEADO"))
            else:
                if not os.path.exists(os.path.join(self.PATH_APP, "datos", "aplicaciones", app, "salida", "BLOQUEADO")):
                    os.mknod(os.path.join(self.PATH_APP, "datos",
                                          "aplicaciones", app, "salida", "BLOQUEADO"))

        for remove_dir in os.listdir(os.path.join(self.PATH_APP, "datos", "aplicaciones")):
            if remove_dir not in self.config["aplicaciones"]:
                shutil.rmtree(os.path.join(self.PATH_APP, "datos",
                                           "aplicaciones", remove_dir), ignore_errors=True)
