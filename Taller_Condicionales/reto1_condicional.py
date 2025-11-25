import random
dado1=random.randint(1,6)
dado2=random.randint(1,6)
print(dado1,dado2)
if dado1%2==0:
    print(f"{dado1} Es par")
else:
    print(f"{dado1} Es impar")
if dado2%2==0:
    print(f"{dado2} Es par")
else:
    print(f"{dado2} Es impar")
if dado1==dado2:
    print("Ganaste")
else:
    print("Game over")
