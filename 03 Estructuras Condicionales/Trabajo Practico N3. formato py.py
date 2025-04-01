# %% [markdown]
# Trabajo Practico N3 - Estudiante: Herrera Gonzalez Franco Esteban.

# %% [markdown]
# Ejercicio 1:

# %%
edad_solicitada = int(input(print("Proporciona tu edad: ")))
if edad_solicitada >= 18 :
    print("es mayor de edad")
else:
    pass

# %% [markdown]
# Ejercicio 2:

# %%
nota_proporcionada = int(input(print("Proporciona tu nota: ")))
if nota_proporcionada >= 6 :
    print("aprobado")
else :
    print("desaprobado")

# %% [markdown]
# Ejercicio 3:

# %%
numero_solicitado = int(input(print("Proporcione un numero par: ")))
if (numero_solicitado % 2 != 0) or (numero_solicitado == 0) :
    print("por favor ingrese un numero par")
else :
    print("Ha ingresado un número par")

# %% [markdown]
# Ejercicio 4:

# %%
edad_solicitada = int(input(print("Proporcione su edad: ")))
if edad_solicitada <= 0  :
    pass
elif edad_solicitada < 12 :
    print("Niño/a")
elif edad_solicitada >= 12 and edad_solicitada < 18 :
    print("Adolecente")
elif edad_solicitada >= 18 and edad_solicitada < 30 :
    print("Adulto/a joven")
else :
    print("Adulto")

# %% [markdown]
# Ejercicio 5:

# %%
contraseña_solicitada = input(print("Proporcione su edad: "))
if len(contraseña_solicitada) >= 8 and len(contraseña_solicitada) <= 14 :
    print("La contraseña es correcta")
else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# %% [markdown]
# Ejercicio 6:

# %%
import random
from statistics import mean, median, mode

numero_aleatorio = [random.randint(1, 100) for i in range(50)]

print(f"media = {mean(numero_aleatorio)}")
print(f"mediana = {median(numero_aleatorio)}")
print(f"moda {mode(numero_aleatorio)}")

# %% [markdown]
# Ejercicio 7:

# %%
palabra_frase = input(print("Propocione un texto: "))
ultimo_caracter = palabra_frase[-1]


if ultimo_caracter == "a" or ultimo_caracter == "e" or ultimo_caracter == "i" or ultimo_caracter == "o" or ultimo_caracter == "u" :
    print(palabra_frase + "!")
else :
    print(palabra_frase)

# %% [markdown]
# Ejercicio 8:

# %%
nombre = input(print("Proporcione su nombre"))
valor = int(input(print("1: NOMBRE \n 2: nombre \n 3: Nombre")))

if valor == 1 :
    print(nombre.upper)
elif valor == 2 :
    print(nombre.lower())
elif valor == 3:
    print(nombre.title())
else :
    pass

# %% [markdown]
# Ejercicio 9

# %%
escala_terremoto = float(input(print("proporcione la escala del terremoto: ")))
if escala_terremoto < 3 :
    print("'muy leve' (imperceptible)")
elif escala_terremoto < 4 :
    print("'leve' (ligeramente perceptible)")
elif escala_terremoto < 5 :
    print("'moderado' (sentido por personas, pero generalmente no causa daños).")
elif escala_terremoto < 6 :
    print("'fuerte' (puede causar daños en estructuras débiles)")
elif escala_terremoto < 7 :
    print("'muy fuerte' (puede causar daños significativos)")
elif escala_terremoto >= 7:
    print("'extremo' (puede causar graves daños a gran escala)")
else :
    pass

# %% [markdown]
# Ejercicio 10:

# %%
hemisferio = input(print("En que hemisferio te encuentras? (N/S)"))
hemisferio = hemisferio.lower()
dia = int(input(print("Que dia del mes es?")))
mes = int(input(print("Que numero de mes es?")))

if hemisferio == "s":
    if mes <= 3 and dia <=20:
        print("verano")
    elif  mes <= 6 and dia <=20:
        print("otoño")
    elif  mes <= 9 and dia <=20:
        print("invierno")
    elif  mes <= 9 and dia <=20:
        print("primavera")
    else:
        print("verano")
elif hemisferio == "n" :
    if mes <= 3 and dia <=20:
        print("invierno")
    elif  mes <= 6 and dia <=20:
        print("primavera")
    elif  mes <= 9 and dia <=20:
        print("verano")
    elif  mes <= 9 and dia <=20:
        print("otoño")
    else:
        print("invierno")
else:
    pass


