# %% [markdown]
# Ejercicio 1

# %%
uno_al_cien = list(range(0, 101, 4))
print(uno_al_cien)

# %% [markdown]
# Ejercicio 2

# %%
cuatro_elementos = ["uno", "dos", "tres", "cuatro"]
print(cuatro_elementos[2])

# %% [markdown]
# Ejercicio 3

# %%
elementos_añadir = []
elementos_añadir.append("hola")
elementos_añadir.append("como")
elementos_añadir.append("estas")
elementos_añadir.append("?")

print(elementos_añadir)

# %% [markdown]
# Ejercicio 4

# %%
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[3] = "oso"
print(animales)

# %% [markdown]
# Ejercicio 5

# %%
numeros = [8, 15, 3, 22, 7] #define una lista con cinco elementos numericos.
numeros.remove(max(numeros)) #elimina el numero mayor de la lista, en este caso el 22.
print(numeros) #imprime la lista, ahora con cuatro elementos ya que el "22" fue eliminado.

# %% [markdown]
# Ejercicio 6

# %%
diez_al_treinta = list(range(10, 31, 5))
for i in range(0,2):
    print(diez_al_treinta[i])

# %% [markdown]
# Ejercicio 7

# %%
autos = ["sedán", "polo", "suran", "gol"]
autos[1] = "corvette"
autos[2] = "ranger"


# %% [markdown]
# Ejercicio 8

# %%
dobles = []
añadir = 5
for i in range(0, 3):
    añadir_doble = añadir*2 
    dobles.append(añadir_doble)
    añadir += 5
print(dobles)

# %% [markdown]
# Ejercicio 9
# 

# %%
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]] 
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# %% [markdown]
# Ejercicio 10

# %%
lista_anidada = ["","",["","",""],""]
lista_anidada[0]= 15 
lista_anidada[1]= True 
lista_anidada[2][0]= 25.5 
lista_anidada[2][1]= 57.9 
lista_anidada[2][2]= 30.6 
lista_anidada[3]= False 

print(lista_anidada)


