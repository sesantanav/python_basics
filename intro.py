"""
Comentarios multilinea
"""

# Comentarios de una linea

if 5 > 2:
    # 
    print("5 es mayor que 2.")


x = 5

y = 'Variable'

print(y)


# Variables ilegales
# 2variable = 'variable ilegal'
# var-variable = 'Mi variable'
# mi var = ''

# Variables legales
_variable = 0
variable = 0
_variab_le = 0
vaRiable = 0

# asignar valores a multiples variables

x , y , z  = "Hola ", "Mundo ", "!"

print(x)
print(y)
print(z)

a = b = c = 0
print(a)
print(b)

print("Mensaje " + x)

m = x + y + z
print(m)


# Variables globales

x = "Programación"

print(x)

def funcion1():
    global x
    x = "Base de Datos"
    print("Taller de " + x)

funcion1()

print(x)
