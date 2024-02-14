# 4.Realizar un programa que filtre si eres apto para registrar un negocio ,condiciones: mayor de edad, tener ruc y tener un nombre comercial,
# los inputs son si y /o no. la salida debe ser si esta apto o no para abrir un comercio.

print("Bienvenidos")

Edad = (input("Es mayor de Edad? (Si/No) "))
RUC = input("Cuenta con RUC? (Si/No) ")
NombreComercial = input("Cuenta con Nombre Comercial? (Si/No) ")

if (Edad != "No" and RUC != "No" and NombreComercial != "No"):
    apto = "Si"
else:
    apto = "No"

msg = f"Usted {apto} es apto para abrir un Comercio"

print(msg)






print("Bienvenidos")

Edad = int(input("Cual es tu edad? "))
RUC = input("Introduzca su RUC, escriba No si no tiene: ")
NombreComercial = input("Brindar nombre Comercial, escriba No si no tiene: ")

if (Edad >= 18 and RUC != "No" and NombreComercial != "No"):
    apto = "Si"
else:
    apto = "No"

msg = f"Usted {apto} es apto para abrir un Comercio"

print(msg)