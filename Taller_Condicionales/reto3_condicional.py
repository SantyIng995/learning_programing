num=int(input("Ingresar numero:"))
if num%2==0:
    if num<0:
        print("El numero es negativo y es par")
    elif num>0:
        print("EL numero es positivo y es par")
else:
    if num<0:
        print("El numero es negativo y es impar")
    elif num>0:
        print("EL numero es positivo y es impar")