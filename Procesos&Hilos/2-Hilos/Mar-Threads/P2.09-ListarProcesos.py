import threading
import time

def tarea():
    time.sleep(1)
    return

for _ in range(10):
    threading.Thread(target=tarea).start()

print ("Hilos activos: ",threading.active_count())    # 11 hios activos, el principal y 10 hilos
for thread in threading.enumerate():                  #enumera todos los hilos q se estan ejecutando
    print(thread.name)