import threading

def tarea(numero):
    print(f'Numero de Hilo {numero} ')

hilos = []
for i in range(1,200):
    hilo = threading.Thread(target= tarea , args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

