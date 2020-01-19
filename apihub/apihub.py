# import pdb

from configuracion import PATH_APP
from sistema_ficheros import SistemaFicheros


# config = {}


sf = SistemaFicheros(PATH_APP)


config = sf.cargar_configuracion()

print(config)

# pdb.set_trace()

sf.enrutar_archivos()

# sf.actualiza_estructura()

# sf.guardar_configuracion()
