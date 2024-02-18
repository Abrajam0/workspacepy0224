import random

def call_inputs():
    a = int(input("ingrese la Numero 1: "))
    b = int(input("ingrese la Numero 2: "))
    return (a, b)

def calcular_promedio(notas):
            return sum(notas) / len(notas)

control=0
alumnos_aprobados = []
alumnos_desaprobados = []
notas_finales = []



while True:
    print("Bienvenidos")
    opciones = """ 
        1. Datos personales
        2. Operaciones matematicas basicas
        3. Cursos
        4. Promedio general
        5. Alumnos aprobados
        6. Alumnos Desaprobados
        7. Numeros multiplos de 2,5,7
        8. Numero mayor?
        9. Salir
    """
    print(opciones)
    opc = int(input("Ingrese la opcion: "))
    if opc == 1:
        nombre = input("Ingrese su nombre: ")
        DNI = input("Ingrese su DNI: ")
        Cumpleaños = input("Ingrese Cumpleaños: ")
        Edad = int(input("Ingrese su edad: "))
        Direccion = input("Ingrese su direccion: ")
        correo = input("Ingrese correo: ")
        print("nombre: ", nombre, "\n"+ "DNI", DNI, "\n"+ "Cumpleaños", "\n"+"Edad", Edad, "\n"+"Direccion", Direccion)
        correccion = input("La informacion es correcta? (Si/No): ")
        if correccion.upper() == "NO":
            print("Vuelva a ingresar datos: ")
        else:
            msg = f"Bienvenido {nombre} de {Edad} de edad con vivienda en {Direccion}"
            print(msg)
        control=1
    
    elif opc == 2:

        opciones1 = """ 
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
        """
        print(opciones1)
        opc1 = int(input("Ingrese opcion: "))
        numeros = call_inputs()
        if opc1 == 1:
            operacion = numeros [0] + numeros[1]
            msg = f"La suma es {operacion}"
            print(msg)
        elif opc1 == 2:
            operacion = numeros [0] - numeros[1]
            msg = f"La resta es {operacion}"
            print(msg)
        elif opc1 == 3:
            operacion = numeros [0] * numeros[1]
            msg = f"La multiplicacion es {operacion}"
            print(msg)
        elif opc1 == 4:
            operacion = numeros [0] / numeros[1]
            msg = f"La division es {operacion}"
            print(msg)
        else: 
            print("Error")
    
    elif opc == 3:
        if control == 1:
            dic = {
                'Nombre': nombre,
                'Edad': Edad,
                'Correo': correo,
                'Cursos': {"Lenguaje": {"codigo": {'0001'} , 'notas': {random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),random.randint(1, 20)}}, 
                           "Redaccion": {"codigo": {'0002'} , 'notas': {random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),random.randint(1, 20)}}, 
                           "Matematicas": {"codigo": {'0003'} , 'notas': {random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),random.randint(1, 20)}},
                           "LC": {"codigo": {'0004'} , 'notas': {random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),random.randint(1, 20),random.randint(1, 20)}}}
            }
        else:
            print("No ingreso datos")
            continue
        print(dic)
        control = 2
    
    elif opc == 4:
        if control == 2:
            todas_las_notas = set()

            for detalles in dic['Cursos'].values():
                todas_las_notas.update(detalles['notas'])

            promedio_general = calcular_promedio(todas_las_notas)
            notas_finales.append(promedio_general)

            print(f"Promedio General: {promedio_general}")
        else:
            print("No ingreso datos")
            continue
        control = 3

    elif opc == 5:
        if control == 3:
            if promedio_general >= 10.5:
                alumnos_aprobados.append(nombre)
        print(alumnos_aprobados)

    elif opc == 6:
        if control == 3:
            if promedio_general < 10.5:
                alumnos_desaprobados.append(nombre)
        print(alumnos_desaprobados)
    
    elif opc == 7:
        rango = int(input("ingrese numero maximo 10^10: "))
        step = int(input("ingrese saltos: "))
        if rango > 10 ** 10:
            rango = 10 ** 10
        
        def generar_lista_multiplos(rango, step=1):
            lista_resultado = []

            for num in range(1, rango + 1, step):
                if num % 2 == 0 or num % 5 == 0 or num % 7 == 0:
                    lista_resultado.append(num)

            return lista_resultado
        lista = generar_lista_multiplos(rango, step)
        print(lista)
    
    elif opc == 8:
        numero1 = int(input("Ingrese numero 1: "))
        numero2 = int(input("Ingrese numero 2: "))
        if numero1 > numero2:
            final = numero1
        else: 
            final = numero2
        msg = f"El numero mayor es {final}"
        print(msg)

    elif opc == 9:
        break
    else:
        print("Error")
