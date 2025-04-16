##Trabajo Practico Funciones - Herrera Gonzalez Franco Esteban.

##Ejercicio N1:
def imprimir_hola_mundo():
        print("Hola mundo!")

imprimir_hola_mundo()

##Ejercicio N2:
def saludar_usuario(nombre):
        print(f"hola {nombre}!")

saludar_usuario("Marcos")

##Ejercicio N3:
def informacion_personal(nombre, apellido, edad, residencia):
        print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("proporcione su nombre: ")
apellido = input("proporcione su apellido: ")
edad = input("proporcione su edad: ")
residencia = input("proporcione su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

##Ejercicio N4
def calcular_area_circulo(radio):
        from math import pi
        area = pi * (radio)**2
        print(f"el area del circulo con radio de {radio}cm es de {area}cm")

def calcular_perimetro_circulo(radio):
        from math import pi
        perimetro = pi * radio*2
        print(f"el perimetro del circulo con radio de {radio}cm es de {perimetro}cm")

radio = float(input("proporcione el radio en cm: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

##Ejercicio N5
def segundos_a_horas(segundos):
        horas = (segundos/60)/60
        print(f"La cantidad de horas equivalentes a {segundos} segundos es {horas}")

segundos_a_horas(float(input("propocione una cantidad de segundos: ")))

##Ejercicio N6
def tabla_multiplicar(numero):
        for i in range(1, 11):
                print(f"{i} x {numero} = {i*numero}")

tabla_multiplicar(int(input("proporcione un numero: ")))

#Ejercicio N7
def operaciones_basicas(a, b):
        print(f"{a} + {b} = {a + b}")
        print(f"{a} - {b} = {a - b}")
        print(f"{a} / {b} = {a / b}")
        print(f"{a} * {b} = {a * b}")

a = int(input("Proporcione el valor 'A': "))
b = int(input("Proporcione el valor 'B': "))
operaciones_basicas(a, b)

#Ejercicio N8
def calcular_imc(peso, altura):
        imc = peso / altura
        imc = round(imc, 2)
        print(f"el indice de masa corporal es de {imc}")
        
peso = float(input("Proporcione su peso: "))
altura = float(input("Proporcione su altura: "))
calcular_imc(peso, altura)

#Ejercicio N9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")

celsius_a_fahrenheit(float(input("proporcione la temperatura en celsius: ")))

#Ejercicio N10
def calcular_promedio(a, b, c):
        promedio = (a + b + c)/3
        print(f"el promedio de {a}, {b}, y {c} es: {promedio}")

valor_a = float(input("Proporcione un valor: "))
valor_b = float(input("Proporcione un valor: "))
valor_c = float(input("Proporcione un valor: "))

calcular_promedio(valor_a, valor_b, valor_c)