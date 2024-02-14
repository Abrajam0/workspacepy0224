# 3.Realizar un programa que nos pida el ingreso total de un hogar y vaya pidiendo posibles gastos. 
# Como resultado debe decir  todos los egresos y el ahorro.


print("Bienvenidos, nos encargaremos de medir sus egresos y ahorro (ser lo mas breve posible)")

IngresoNeto = float(input("A cuanto asciende su ingreso neto?  "))

Comida = int(input("Gasto en Comida: "))
Ropa = int(input("Gasto en Ropa: "))
Intereses = int(input("Gasto en Intereses: "))
Alquiler = int(input("Gasto en Alquiler o Hipoteca: "))

egresos = Comida + Ropa + Intereses + Alquiler
Ahorro = IngresoNeto - egresos

msg = f"Sus Egresos fueron {egresos} y su ahorro fue de {Ahorro}"

print(msg)