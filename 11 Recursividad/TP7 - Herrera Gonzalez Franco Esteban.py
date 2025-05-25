# %% [markdown]
# ## TP 7
# Estudiante: Herrera Gonzalez Franco Esteban

# %% [markdown]
# ## Ejercicio 1
# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

# %%
def factorial_recu(n):
    if n==1:
        return 1
    else:
        return n * factorial_recu(n-1)


x = int(input("proporcione un numero entero positivo para generar su factorial: "))
print(factorial_recu(x))

# %% [markdown]
# ## Ejercicio 2
# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

# %%
def fibonacci_recu(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recu(posicion-1) + fibonacci_recu(posicion-2)
    
pos = int(input("proporcione la posicion de fibonacci que desea calcular: "))
print(fibonacci_recu(pos))

# %% [markdown]
# ## Ejercicio 3
# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un 
# algoritmo general. 

# %%
def potencia_recursiva(n, m):
    if m == 1:
        return n
    else:
        return n * potencia_recursiva(n, m-1)

n = int(input("proporcione un numero base: "))
m = int(input("proporcione un exponente: "))
print(potencia_recursiva(n,m))

# %% [markdown]
# ## Ejercicio 4
# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

# %%
def binario_recursivo(numero):
    if numero <= 0:
        return ""
    else:
        caracter = str(numero % 2)
        caracter2 = binario_recursivo(int(numero/2))
        return caracter2 + caracter

numero = int(input("proporcione un numero decimal: "))
print(f"{numero} en binario es {binario_recursivo(numero)}")

# %% [markdown]
# ## Ejercicio 5
# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 

# %%
def es_palindromo(palabra):
    if len(palabra) < 2:
        return True
    elif palabra[0] != palabra[len(palabra)-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])



p = input("proporcione una palabra: ")
print(es_palindromo(p))     

# %% [markdown]
# ## Ejercicio 6
# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

# %%
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

x = int(input("proporcione un numero entero"))
print(suma_digitos(x))

# %% [markdown]
# ## Ejercicio 7
# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
#  
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
#  
#       Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

# %%
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
    
n = int(input("proporcione un numero de bloques para la base: "))
print(contar_bloques(n))

# %% [markdown]
# ## Ejercicio 8
# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
#       Ejemplos: 
# 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0   

# %%
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_d = numero % 10
        if ultimo_d == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


n = int(input("propocione un numero a evaluar: "))
d = int(input("proporcione el digito a evaluar: "))
print(contar_digito(n, d))  
            


