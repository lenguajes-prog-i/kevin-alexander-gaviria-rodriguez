import pickle

def crear_auto(modelo, placa):
    return {"modelo": modelo, "placa": placa}

def mostrar_auto(auto):
    return f"El auto {auto['modelo']} tiene placa {auto['placa']}"

def guardar_autos(autos, archivo):
    with open(archivo, "wb") as f:
        return pickle.dump(autos,f)

def leer_autos(archivo):
    with open(archivo, "rb") as f: 
        return pickle.load(f)

autos = [
    crear_auto("Mazda", "ABC123"),
    crear_auto("Toyota", "ABC153"),
    crear_auto("Ferrari", "ABC113"),
    crear_auto("Bmw", "ABC143"),
    crear_auto("Mitsubishi", "ABC020")
]

guardar_autos(autos, "autos.pkl")

autos_leidos = leer_autos("autos.pkl")

for texto in map(mostrar_auto, autos_leidos):
    print(texto)

