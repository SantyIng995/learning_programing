import random

def lanzar_dado():
    return random.randint(1, 6)

def reto6():
    total_tiros = 0
    suma_total = 0
    pares = 0
    impares = 0

    respuesta = "s"

    while respuesta.lower() == "s":
        dado = lanzar_dado()
        total_tiros += 1
        suma_total += dado

        print(f"Tiro {total_tiros}: {dado}")

        if dado % 2 == 0:
            pares += 1
        else:
            impares += 1

        respuesta = input("¿Desea volver a lanzar? (s/n): ")

    print("REPORTE FINAL")
    print(f"Total de tiros efectuados: {total_tiros}")
    print(f"Suma total de los tiros: {suma_total}")
    print(f"Total de pares generados: {pares}")
    print(f"Total de impares generados: {impares}")
reto6()
