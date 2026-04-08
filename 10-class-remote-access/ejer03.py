import pickle

class Auto:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

    def __repr__(self):
        return f"El auto {self.modelo} tiene placa {self.placa}"

# Crear objetos
objeto_auto = Auto("Mazda", "ABC123")
objeto_auto1 = Auto("Toyota", "ABC153")
objeto_auto2 = Auto("Ferrari", "ABC113")
objeto_auto3 = Auto("Bmw", "ABC143")
objeto_auto4 = Auto("Hilux", "ABC124")

# Guardarlos en una lista
lista_autos = [objeto_auto, objeto_auto1, objeto_auto2, objeto_auto3, objeto_auto4]

# Escritura del archivo
with open("autos.txt", "wb") as archivo_auto:
    pickle.dump(lista_autos, archivo_auto)

# Lectura del archivo
with open("autos.txt", "rb") as archivo_auto:
    autos = pickle.load(archivo_auto)

# Mostrar los autos
for auto in autos:
    print(auto)