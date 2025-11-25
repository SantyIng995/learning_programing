import random
contador=0
print("lanzando dados hasta obtener un 6")
while True:
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    contador += 1
    print(f"Tiro {contador} Dado1 = {dado1} Dado2 ={dado2}")
    if dado1 == 6 and dado2 == 6:
        print("¡Par de seis obtenido!")
        print(f"Total de lanzamientos: {contador}")
        break
    