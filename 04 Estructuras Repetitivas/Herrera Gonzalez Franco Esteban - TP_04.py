# %% [markdown]
# Ejercicio 1:

# %%
for i in range(0, 101): ##iterar i desde 0 hasta 100
    print(i)    ##imprimir i  

# %% [markdown]
# Ejercicio 2:

# %%
num = int(input("proporcione un numero entero")) #dato ingresado por el usuario, forzado a ser entero.
num = str(num)  #se transforma en string para ser procesado por la funcion len
cantidad_digitos = len(num) #la funcion len cuenta la cantidad de digitos del numero proporcionado
print(f"la cantidad de digitos del numero proporcionado es de: {cantidad_digitos}") #se imprime el resultado final

# %% [markdown]
# Ejercicio 3:

# %%
inicio = int(input("proporcione el numero entero inicial: "))
fin = int(input("proporcione el numero entero final: "))
sumatoria = 0
if inicio < fin :
    for i in range(inicio + 1, fin):
        sumatoria = sumatoria + i
else:
    for i in range(inicio - 1, fin, -1):
        sumatoria = sumatoria + i
print(f"sumatoria {sumatoria}")

# %% [markdown]
# Ejercicio 4:

# %%
suma = 0
num_uno = int(input("proporcione un numero entero para sumar (ingrese 0 para terminar)"))
while num_uno != 0:
    suma = num_uno + suma
    num_uno = int(input("proporcione un numero entero para sumar (ingrese 0 para terminar)"))
print(f"suma total = {suma}")

# %% [markdown]
# Ejercicio 5:

# %%
import random
numero_adivinar = random.randint(0,9)
cant_intentos = 0
adivinar = int(input("Adivine el numero(0 a 9): "))
while adivinar != numero_adivinar:
    cant_intentos = cant_intentos + 1
    adivinar = int(input("Adivine el numero(0 a 9): "))
print(f"numero correcto = {numero_adivinar}")
print(f"cantidad de intentos = {cant_intentos}")

# %% [markdown]
# Ejercicio 6:

# %%
for i in range(99, 0, -1):
    if i % 2 == 0:
        print(i)

# %% [markdown]
# Ejercicio 7:

# %%
final_rango = int(input("Proporcione un valor final para el rango: "))
sumar = 0
if 0 < final_rango:
    for i in range(0, final_rango):
        sumar = sumar + i
else:
    for i in range(0, final_rango, -1):
        sumar = sumar + i
print(f"la suma de los numeros entre 0 y {final_rango} es: {sumar}")

# %% [markdown]
# Ejercicio 8:

# %%
pares = 0
impares = 0
negativos = 0
positivos = 0
k = int(input("proporcione un numero:"))
for i in range(0, 100):
    if k == 0:
        pass
    elif k % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    if k == 0:
        pass
    elif k < 0:
        negativos = negativos + 1
    else:
        positivos = positivos + 1
    k = int(input("proporcione un numero:"))

print(f"numero pares: {pares}")
print(f"numero impares: {impares}")
print(f"numero positivos: {positivos}")
print(f"numero negativos: {negativos}")

# %% [markdown]
# Ejercicio 9:

# %%
cant_valores = int(100)
sum = int(0)
for i in range (0, cant_valores):
    nume = int(input("proporcione un numero"))
    sum = sum + nume
print(f"el promedio de los {cant_valores} numeros es de: {sum/cant_valores}")

# %% [markdown]
# Ejercicio 10:

# %%
numero = 0
numero_invertido = 0
numero = input("Ingrese un número: ")
if int(numero) > 0:
    numero_invertido = numero[::-1]
elif int(numero) < 0 :
    numero_invertido = '-' + numero[:0:-1]
else:
    pass
print(f"El número invertido es: {numero_invertido}")

# %% [markdown]
# Estudiante: Herrera Gonzalez Franco Esteban


