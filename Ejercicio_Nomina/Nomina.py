total_empleados = 0
total_m = 0
total_f = 0
total_o = 0
total_salarios = 0
suma_edades = 0

while True:
    operacion = input("Desea agregar empleado? (S/N): ").upper()
    if operacion == "N":
        break
    elif operacion != "S":
        print("Opción inválida. Responda con S o N.")
        continue
    
    print("\nRegistro de empleado")

    nombre = input("Nombres completos: ")
    email = input("Email: ")
    numero = input("Número móvil: ")

    genero = input("Género [M-F-O]: ").upper()
    while genero not in ["M", "F", "O"]:
        print("Género inválido. Solo se acepta M, F u O.")
        genero = input("Género [M-F-O]: ").upper()
    salario = float(input("Salario: "))

    from datetime import datetime
    while True:
        nacimiento = input("Año de nacimiento [AAAA]: ")
        nacimiento = int(nacimiento)
        año_actual = datetime.now().year
        edad = año_actual - nacimiento
        print(f"La edad del empleado es: {edad} años")
        if edad < 18:
            print("El empleado debe ser mayor de 18 años.")
        else:
            break

    total_empleados += 1
    total_salarios += salario
    suma_edades += edad

    if genero == "M":
        total_m += 1
    elif genero == "F":
        total_f += 1
    else:
        total_o += 1

print("\nREPORTE FINAL")
print(f"Total de empleados registrados: {total_empleados}")
print(f"Total género M: {total_m}")
print(f"Total género F: {total_f}")
print(f"Total género O: {total_o}")
print(f"Total salarios a pagar: ${total_salarios}")
print(f"Promedio de edades: {suma_edades / total_empleados:.2f}")