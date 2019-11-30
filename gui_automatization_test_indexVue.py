import pyautogui
import time
import os


SEGUNDOS_CARGA_PAGINA = 1
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# pyautogui.displayMousePosition() #Display real time mouse position.
# print(pyautogui.size())
# width, height = pyautogui.size()
# mouse_position = pyautogui.position()
# x, y = mouse_position
# print(x,y)
#pyautogui.moveTo(10,10, duration=1)
# pyautogui.moveRel(200,0,1)
# pyautogui.click(997,304)
# pyautogui.doubleClick(997,304)
# print(pyautogui.KEYBOARD_KEYS)
# pyautogui.press("f1")
# pyautogui.hotkey('ctrl','a')

w, h = pyautogui.size()

if not (w == 1920 and h == 1080):
    print("Error: La resolución debe ser 1920x1080")
    exit(1)


def now():
    return time.strftime("%Y%m%d%H%M%S", time.gmtime())


def pantallazo(nombre_test):

    directorio = os.path.join(ROOT_DIR, "tests", nombre_test)
    fichero = now() + "_" + nombre_test.upper() + ".png"
    fichero = os.path.join(directorio, "resultado", fichero)

    pyautogui.screenshot(fichero)

def pru():
    from tkinter import Tk
    root = Tk()
    root.withdraw()
    
    pyautogui.doubleClick(782,211)
    pyautogui.hotkey('ctrl','c')

    print("pues sale", root.clipboard_get())

    pyautogui.doubleClick(782,316)
    pyautogui.hotkey('ctrl','c')

    x = root.clipboard_get()
    
    
    print("y ahora", str(x).upper())



def test_login():
    
    fichero = os.path.join(ROOT_DIR, "tests", "login", "control_de_acceso.png")
    
    # if not pyautogui.locateOnScreen(fichero):
    #     print("Error: Debo estar posicionado en la pantalla de control de acceso y maximizado f11")
    #     pantallazo("login")
    #     exit(1)
    
    pyautogui.click(920, 264)   # Me posiciono en el campo usuario
    pyautogui.typewrite("juanra", interval=0.1)
    pyautogui.press("tab")      # Tabulo al campo password
    pyautogui.typewrite("juanra", interval=0.1)
    pyautogui.press("enter")

    time.sleep(SEGUNDOS_CARGA_PAGINA)

    fichero = os.path.join(ROOT_DIR, "tests", "login", "sesion_juanra.png")
    
    if pyautogui.locateOnScreen(fichero):
        print("resultado OK")
    else:
        print("No va!! :'(")

    pantallazo("login")


def main():
    # test_login()
    pru()

    exit(0)


if __name__ == "__main__":
    main()
