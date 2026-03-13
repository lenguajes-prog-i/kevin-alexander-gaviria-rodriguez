numero1 = float(input("Ingrese el número 1: "))
numero2 = float(input("Ingrese el número 2: "))

print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Opción: ")

if opcion == "1":
    print("La suma es:", numero1 + numero2)
elif opcion == "2":
    print("La resta es:", numero1 - numero2)
elif opcion == "3":
    print("La multiplicación es:", numero1 * numero2)
elif opcion == "4":
    if numero2 != 0:
        print("La división es:", numero1 / numero2)
    else:
        print("No se puede dividir entre cero.")
else:
    print("Opción no válida.")