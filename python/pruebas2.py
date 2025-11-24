import random

contadorPares = 0
contadorImpares = 0
totalTiros = 0
sumaTiros = 0

while True:
    print("¿Deseas lanzar el dado? (s/n)")
    respuesta = input().lower()

    if respuesta != 's':
        print("\n¡Gracias por jugar!")
        break

    numero = random.randint(1, 6)
    print(f"Número obtenido: {numero}")

    
    totalTiros += 1
    sumaTiros += numero

    if numero % 2 == 0:
        contadorPares += 1
    else:
        contadorImpares += 1


print("\n--- REPORTE FINAL ---")
print(f"Total de tiros efectuados: {totalTiros}")
print(f"Suma total de los tiros: {sumaTiros}")
print(f"Total de pares generados: {contadorPares}")
print(f"Total de impares generados: {contadorImpares}")
