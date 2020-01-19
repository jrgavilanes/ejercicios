from datetime import datetime
import os

from configuracion import PATH_APP


class Log:

    DATOS_LOG = os.path.join(PATH_APP, "datos", "log")

    @classmethod
    def escribe_log(cls, modulo: str, funcion: str, mensaje: str, tipo="INFO"):
        """
        Escribe mensaje en fichero en ./log/{modulo}_AAAAMMDD.log

        Args:
            modulo (str): nombre del fichero que contiene la funcion
            funcion (str): nombre de la funcion que hace la llamada. No poner ()
            mensaje (str): texto a indicar en el log
            tipo (str): [defecto "INFO", "WARNING", "ERROR"]

        Retorno:
            None        
        """

        ahora = datetime.now()
        fichero = "{}_{}{:02d}{:02d}.log".format(modulo,
                                                 ahora.year,
                                                 ahora.month,
                                                 ahora.day)
        fichero = os.path.join(cls.DATOS_LOG, fichero)
        msn = "{}::{}::{}::{}".format(ahora, tipo, funcion, mensaje)
        
        if os.system(f"echo {msn} >> {fichero}") == 0:
            return (True, fichero)
        else:
            return (False, fichero)
