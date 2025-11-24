import random
contador1=0
contador2=0
contador3=0
contador4=0
contador5=0
contador6=0
dato= int(input("¿cuantas veces quieres lanzar el dado?"))
for i in range(dato) :
    numero=random.randint(1,6)
    print(numero)
    if numero==1:
        contador1+=1
    elif numero==2:
        contador2+=1
    elif numero==3:
        contador3+=1
    elif numero==4:
        contador4+=1
    elif numero==5:
        contador5+=1
    elif numero==6:
        contador6+=1
print(f"El numero 1 salio:{contador1} veces")
print(f"El numero 2 salio:{contador2} veces")
print(f"El numero 3 salio:{contador3} veces")
print(f"El numero 4 salio:{contador4} veces")
print(f"El numero 5 salio:{contador5} veces")
print(f"El numero 6 salio:{contador6} veces")
print(f"Total valores de los lanzamientos:{dato}")
