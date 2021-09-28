
#Mensaje para el usuario
print("***Programa para una matriz***")
print("Ingrese las dimensiones de la matriz")
print("Valor de columnas y filas")
column = int(input("Columnas : "))
rows = int(input("Filas : "))
#Matriz vacia
Matriz = []
val = [0,1,2,3,4,5,6,7,8,9,10]
for i in range(column):
    Matriz[i].append([])
#llenado de los valores
for i in range(val):
    for j in range(val): 
        Matriz[i].append(eval(input("Valor ", i, " ", j, "de la matriz: ")))

#imprimir matriz
print("La matriz resultate es la siguiente :")
for i in val:
    for j in val:
        print(Matriz[i][j])
    print("\n")
print("\n")

