import threading

def tarea(letra):
    for _ in range(5):
        print(f'Letra de abecedario {letra} ')

hilos = []
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

for i in letras:
    hilo = threading.Thread(target= tarea, args=(i,) )
    hilos.append(hilo)
    hilo.start()

for i in hilos:
    i.join()
