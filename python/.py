gender=input("Genero:")
salary=int(input("Salario:"))
if salary<=1200000 and gender=="mujer":
    salary+=(10*(salary)/100)
    print(salary)
elif salary<=1200000 and gender=="hombre":
    salary+=(8*(salary)/100)
    print(salary)
elif salary>=1200000 and salary<2000000:
    salary+=(5*(salary)/100)
    print(salary)
elif salary>=2000000 and gender=="mujer":
    salary+=(3*(salary)/100)
    print(salary)
elif salary>=2000000 and gender=="hombre":
    salary+=(2.5*(salary)/100)
    print(salary)
