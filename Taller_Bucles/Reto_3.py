import random

dato = int(input("¿Cuántas veces quieres lanzar el dado? "))

contadores = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(dato):
    numero = random.randint(1, 6)
    print(numero)
    contadores[numero] += 1  


print("\n RESULTADOS:")
for num in range(1, 7):
    print(f"El número {num} salió {contadores[num]} veces")
