import random
"""for i in range(1,7):
    print(i)"""
dato= int(input("¿cuantas veces quieres tirar el dado?"))
suma=0
for i in range(dato):
    numero=random.randint(1,6)
    print(numero)
    suma=suma+numero
print(f"Total valores de los lanzamientoa:{suma}")


