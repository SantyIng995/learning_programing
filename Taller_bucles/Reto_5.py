import random

def lanzar_dado():
    return random.randint(1, 6)

def reto5():
    n = int(input("Ingrese el número de lanzamientos: "))

    pares = 0
    impares = 0

    for i in range(1, n + 1):
        dado = lanzar_dado()
        print(f"Lanzamiento {i}: {dado}")

        if dado % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("RESULTADOS")
    print(f"Total de tiros: {n}")
    print(f"Tiros pares: {pares}")
    print(f"Tiros impares: {impares}")
reto5()
