import random
print("lanzamiento de dados")
dato=input("¿Quieres lanzar el dado?")
if dato=="si":
    
    numero=random.randint(1,6)
    print(numero)
    if numero %2==0:
        print("El dado es un numero par")
    else:
        print("El dado es un numero impar")
else: 
    print("No lanzaste")