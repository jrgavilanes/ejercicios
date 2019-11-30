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


def enter():
    pyautogui.press("enter")


def pantallazo(nombre_test):
    directorio = os.path.join(ROOT_DIR, "tests", nombre_test)

    if not os.path.exists(directorio):
        try:
            os.makedirs(os.path.join(ROOT_DIR, "tests"))
        except FileExistsError:
            pass

        os.makedirs(directorio)

    fichero = now() + "_" + nombre_test.upper() + ".png"
    fichero = os.path.join(directorio, fichero)

    pyautogui.screenshot(fichero)


def test_login_ok():

    if not (selecciona(311, 109) == "Control"):
        print("ERROR: Debe estar en la pantalla de login, maximizado y al 100%")
        exit(1)

    click(920, 264)  # Me posiciono en el campo usuario
    escribe("juanra")
    tabula()
    escribe("juanra")
    enter()

    espera()

    if selecciona(1522, 162) == "Cerrar":
        print("test OK: login_ok")
    else:
        print("TEST KO: login_ok")

    pantallazo("login_ok")


def main():
    test_login_ok()

    root.destroy()  # objeto tk gui

    exit(0)


if __name__ == "__main__":
    main()
