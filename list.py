# Arrays
"""
List: es ordenada y permite cambiar sus elementos. Permite duplicacos
Tuples: es ordenada y es inmutable. Permite duplicados
Set: no son ordenados, ni indexados. No permite duplicados
Dictionary: no ordenados, permite cambiar elementos y es indexado. No permite duplicados
"""

# List

# Definir una lista
lista = ["perro", "gato", "conejo"]

# Ingresar a los elementos de una lista

print(lista)

print(lista[0])

for x in lista:
    print(x)

# Indices negativos

print("\n")

print(lista[-1])
print(lista[-2])

# Rangos de valores
print("\n")

lista2 = ["lista", "arrays", "tuplas", "set", "dictionary", "value", "key", "index"]

print(lista2[0:4])
print(lista2[:4])
print(lista2[2:])

print(lista2[-6:-3])

# Cabiar el valor de un item

lista2[1] = "while"
print(lista2)

if "while" in lista2:
    print("Existe")

existe = "set"
if existe in lista2:
    print("Existe")

# Largo de una lista

print(len(lista2))

# Agreagar elementos a una lista

lista2.append("insert")
print(lista2)

lista2.insert(1,"item")
print(lista2)

lista2.insert(0, "object")
print(lista2)