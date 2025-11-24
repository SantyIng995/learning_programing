import random
contadorPares=0
contadorImpares=0
while True:
    print("¿Deseas lanzar el dado? (s/n)")
    respuesta = input().lower()
    if respuesta != 's':
        print("¡Gracias por jugar!")
        break
    numero=random.randint(1,6)
    print(f"Número obtenido: {numero}")