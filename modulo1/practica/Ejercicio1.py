## 1.Realizar un programa que pida tus datos personales y mostrar en pantalla los datos solisitados

print("Bienvenidos")

Nombre = input("Ingrese su nombre: ")
Apellidos = input("Ingrese sus apellidos: ")
FechaNacimiento = input("Ingrese su fecha de nacimiento: ")
Genero = input("Ingrese su genero: ")
DNI = input("Ingrese su DNI: ")
Edad = input("Ingrese su edad: ")


msg = f"""Nombre: {Nombre},
        Apellidos: {Apellidos},
        Fecha de Nacimiento: {FechaNacimiento},
        Genero: {Genero},
        DNI: {DNI},
        Edad: {Edad}"""

print(msg)

Correcto = input("La informacion es correcta? (Si/No): ")

if Correcto == "Si":
    print("Gracias")
else:
    print("Vuelva a rellenar por favor!")
