import pyautogui
import time
import os

# Esto es para obtener datos del clipboard.
from tkinter import Tk
root = Tk()
root.withdraw()

# Configuracion
SEGUNDOS_CARGA_PAGINA = 1
SEGUNDOS_MOVIMIENTO_RATON = 0.5
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OFFSET_X, OFFSET_Y = (0, 0)

# pyautogui.displayMousePosition() # Utilidad Display real time mouse position.

w, h = pyautogui.size()

if not (w == 1920 and h == 1080):
    print("Error: LA RESOLUCION DEBE SER 1920x1080")
    exit(1)


def now():
    return time.strftime("%Y%m%d%H%M%S", time.gmtime())


def click(x, y):
    pyautogui.moveTo(x+OFFSET_X, y+OFFSET_Y,
                     duration=SEGUNDOS_MOVIMIENTO_RATON)
    pyautogui.click(x+OFFSET_X, y+OFFSET_Y)


def selecciona(x, y):
    pyautogui.doubleClick(x+OFFSET_X, y+OFFSET_Y)
    pyautogui.hotkey('ctrl', 'c')

    return str(root.clipboard_get()).strip()


def escribe(texto):
    pyautogui.typewrite(texto, interval=0.1)


def espera():
    time.sleep(SEGUNDOS_CARGA_PAGINA)


def tabula():
    pyautogui.press("tab")


def refresca():
    pyautogui.press("f5")


def enter():
    pyautogui.press("enter")


def pantallazo(nombre_test):
    directorio = os.path.join(ROOT_DIR, "tests")

    if not os.path.exists(directorio):
        os.makedirs(directorio)

    fichero = now() + "_" + nombre_test.upper() + ".png"
    fichero = os.path.join(directorio, fichero)

    pyautogui.screenshot(fichero)


def test_login_ok():

    refresca()

    if not (selecciona(311, 109) == "Control"):
        print("ERROR: Debe estar en la pantalla de login, maximizado y al 100%")
        exit(1)

    # Me posiciono en el campo usuario
    click(920, 264)
    escribe("juanra")
    tabula()
    escribe("juanra")
    enter()

    espera()

    if selecciona(468, 414) == "dolores":
        print("test OK: login_ok")
    else:
        print("TEST KO: login_ok")

    pantallazo("login_ok")


def test_login_ko_clave_equivocada():

    if not (selecciona(311, 109) == "Control"):
        print("ERROR: Debe estar en la pantalla de login, maximizado y al 100%")
        exit(1)

    # Me posiciono en el campo usuario
    click(920, 264)
    escribe("juanra")
    tabula()
    escribe("clave_mala")
    enter()

    espera()

    pantallazo("login_ko_clave_equivocada")

    if selecciona(311, 109) == "Control":
        print("test OK: login_ko_clave_equivocada")
    else:
        print("TEST KO: login_ko_clave_equivocada")

    # Me posiciono en el campo usuario
    click(920, 264)


def test_crear_registro():

    # Le doy al botón +
    click(1850, 1011)
    espera()
    # voy al primer campo
    click(373, 263)
    escribe("titulo de algo")
    tabula()
    escribe("incidencia 12345")
    tabula()
    tabula()
    escribe("nueva etiqueta")
    # pincho primer tag
    click(364, 631)
    tabula()
    escribe("relleno sintomas")
    # pincho barra desplazamiento
    click(1912, 1046)
    # selecciono campo procedimiento
    click(420, 710)
    escribe("relleno procedimiento")
    # pincho en guardar
    click(1560, 1041)
    pantallazo("crear_registro")
    # pincho en volver atras
    click(353, 1037)
    espera()
    # estoy en pantalla principal y pincho en buscador
    click(370, 125)
    escribe("algo")
    espera()
    pantallazo("buscador_encuentra")

    if selecciona(435, 378) == "sintomas":
        print("test OK: crear_registro")
    else:
        print("TEST KO: crear_registro")


def test_editar_registro():

    # Le doy al botón editar
    click(1581, 267)
    espera()
    # voy al primer campo y le añado una "x" al final
    click(643, 293)
    escribe("x")
    tabula()
    # pincho barra desplazamiento
    click(1912, 1046)
    # pincho en guardar
    click(1560, 1041)
    pantallazo("editar_registro")
    # pincho en volver atras
    click(353, 1037)
    espera()
    # estoy en pantalla principal y pincho en buscador
    click(370, 125)
    escribe("algox")
    espera()
    pantallazo("buscador_encuentra")

    if selecciona(435, 378) == "sintomas":
        print("test OK: editar_registro")
    else:
        print("TEST KO: editar_registro")


def test_borrar_registro():

    # Le doy al botón editar
    click(1581, 267)
    espera()
    # Le doy al botón borrar documento
    click(1597, 245)
    pantallazo("borrar_registro")
    enter()
    espera()
    # estoy en pantalla principal y refresco datos
    click(341, 70)
    # pincho en buscador
    click(370, 125)
    escribe("algox")
    espera()

    if selecciona(573, 268) == "ningún":
        print("test OK: borrar_registro")
    else:
        print("TEST KO: borrar_registro")

    pantallazo("no_existe_registro")


def test_cerrar_sesion():
    # Le doy al botón editar
    click(1565, 173)

    espera()
    pantallazo("cerrar_sesion")

    if selecciona(311, 109) == "Control":
        print("test OK: cerrar_sesion")
    else:
        print("TEST KO: cerrar_sesion")


def main():
    test_login_ko_clave_equivocada()
    test_login_ok()
    test_crear_registro()
    test_editar_registro()
    test_borrar_registro()
    test_cerrar_sesion()

    # objeto tk gui
    root.destroy()
    exit(0)


if __name__ == "__main__":
    main()
