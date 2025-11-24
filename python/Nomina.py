contadorTrabajadores=0
contadorM=0
contadorF=0
contadorO=0
acumladorSalarios=0
acumuladorEdades=0
while True:   
    print ("Ingrese los datos del empleado")
    dc=input("Nombres Completos:")
    email=input("Correo Electronico:")
    while True:
        movil=int(input("Numero de Celular:"))
        if len(str(movil))==10:
            int(movil) 
            break
        else:   
            print("El numero de celular debe tener 10 digitos. Intenta de nuevo.\n")
    while True:
        genero = input("Genero [M, F, O]: ").upper()

        if genero in ("M", "F", "O"):
            if genero == "M":
                contadorM += 1
            elif genero == "F":
                contadorF += 1
            else:
                contadorO += 1
            break
        else:
            print("Genero no válido, Intenta de nuevo.\n")
    print("Género ingresado:", genero)   
    salary=int(input("Salario Mensual:"))
    from datetime import datetime
    year=int(input("Año de nacimiento:"))
    año_nac=datetime.now().year
    edad=año_nac - int(year)
    while True:
        if edad<18:
            print("El empleado debe ser mayor de edad. Intenta de nuevo.\n")
            year=int(input("Año de nacimiento:"))
            edad=año_nac - int(year)
        else:
            break
    acumuladorEdades += edad
    print(f"La edad es:{edad} años")
    contadorTrabajadores += 1
    acumladorSalarios += salary  
    while True:
        siguiente=input("Desea ingresar otro empleado? [S/N]:").upper()

        if siguiente in ("S"):
            break   
        elif siguiente=="N":
            print("No se ingresaran mas trabajadores")
            print(f"Total de empleados ingresados:{contadorTrabajadores}")
            print(f"Total de empleados Masculinos:{contadorM}")
            print(f"Total de empleados Femeninos:{contadorF}")
            print(f"Total de empleados Otros:{contadorO}")
            print(f"Salario total por pagar a empleados:{acumladorSalarios}")
            print(f"acumulador de edades:{acumuladorEdades/contadorTrabajadores}")
            
