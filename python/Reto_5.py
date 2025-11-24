import random
contadorPares=0
contadorImpares=0
dato= int(input("¿cuantas veces quieres lanzar el dado?"))
for i in range(dato) :
    numero=random.randint(1,6)
    if numero%2==0:
        contadorPares+=1
    else:
        contadorImpares+=1
print(f"El numero de pares es:{contadorPares}")
print(f"El numero de impares es:{contadorImpares}")