# 2.Realizar un programa que calcule el area y el perimetro de un poligono a tu eleccion( triangulo , cuadrado , circulo)

# Area y perimetro de un Cuadrado
print("Calcularemos el area y perimetro de un cuadrado")
Lado = int(input("Colocar altura o base del cuadrado: "))

area = Lado ** 2
perimetro = Lado * 4

msg1 = f"El area del cuadrado es {area} y el perimetro es {perimetro}"

#Area de un Triangulo
print("Calcularemos el area de un triangulo")
Base = int(input("Colocar la base del Triangulo: "))
altura = int(input("Colocar la altura del Triangulo: "))

area = Base * altura / 2

msg2 = f"El area del triangulo es {area}"

#Area y perimetro de un Circulo
print("Calcularemos el area y perimetro de un Circulo")
Radio = int(input("Colocar el radio del circulo: "))

import math
PI=math.pi
area = PI * (Radio ** 2) 
perimetro = 2 * PI * Radio

msg3 = f"El area del circulo es {area} y el perimetro es {perimetro}"

print(msg1, "\n"+ msg2, "\n" + msg3)