nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
nota1 = float(input("Ingresa tu nota: "))
nota2 = float(input("Ingresa tu nota: "))
nota3 = float(input("Ingresa tu nota: "))

result = nota1 + nota2 + nota3
print("Promedio:", result / 3)

if result >= 71:
    print("Aprobado")
else:
    print("No Aprobado")
