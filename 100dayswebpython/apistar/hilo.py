import threading
import time

def create_file():
    x = 1
    while True:
        print("Secundario",x)
        x+=1
        time.sleep(1)

hilo1=threading.Thread(target=create_file, args=(), daemon=True)
hilo1.start()

x = 1
while True:
    print("Primario",x)
    x+=1
    time.sleep(.5)

hilo1.join()
