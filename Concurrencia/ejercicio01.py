import threading
import time

def programar():
    print("inicio 1")
    time.sleep(4)
    print("finalizo 1")

def beber_agua():
    print("inicio 2")
    time.sleep(6)
    print("Finalizo 2")

def estudiar():
    print("inicio 3")
    time.sleep(4)
    print("Finalizo 3")

inicio = time.perf_counter()

# --- Concurrencia
#programar()
#beber_agua()
#estudiar()

#Hilos
hilo_programar = threading.Thread(target= programar,args=())
hilo_programar.start()

hilo_beberagua = threading.Thread(target= beber_agua,args=())
hilo_beberagua.start()

hilo_estudiar = threading.Thread(target= estudiar,args=())
hilo_estudiar.start()

hilo_programar.join()
hilo_beberagua.join()
hilo_estudiar.join()

fin = time.perf_counter()

tiempo = fin - inicio
print(tiempo)

