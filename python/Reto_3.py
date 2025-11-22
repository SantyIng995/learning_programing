import random
dato= int(input("¿cuantas veces quieres lanzar el dado?"))
for i in range(dato) :
    numero=random.randint(1,6)
    print(numero)
