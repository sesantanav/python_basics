# loops 
# while
# for

# While

i = 1

while i <=  6:
    print(i)
    if i == 3:
        break
    i += 1

while i <=  6:
    print(i)
#    if i == 3:
#        continue
    i += 1   

while i < 6:
    print(i)
    i += 1
else:
    print("i no es menor que 6")



# For
m = "Ciclo for"
print(m)

lista = ["Teclado", "Mouse", "Monitor", "CPU"]

for i in lista:
    print(i)
    if i == "Monitor":
        break

palabra = "Teclado"

for i in palabra:
    print(i)

for i in range(2,10,2):
    print(i)
else:
    print("Ejecución finalizada \n")

lista = ["Teclado", "Mouse", "Monitor"]
lista2 = ["pequeño", "mediano", "grande"]

for i in lista:
    for j in lista2:
        print(i,j) 

for i in range(3):
    for j in range(3):
        print(0)