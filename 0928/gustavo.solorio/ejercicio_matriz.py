#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
#Autores: Gustavo Alejandro Solorio Ramos & Eugenio Alejandro Ruiz Mejia

print("***Programa para llenar una lista NxM definida por el usuario***\n")
#Se inicializan los indices para recorrer el arreglo
indice_columna=0
indice_fila=0
dato_ingresado=0;
#Se pide al usuario ingresar el tamaño de la lista
N = eval(input("Ingresa el numero de Columnas: "))
M = eval(input("Ingresa el numero de Filas: "))

#Se define la matriz, la cual se modificará en tamaño mas adelante
matriz = []

#Con los datos ingresados por el usuario, se recorre la lista primero por filas
while indice_fila<M:
    matriz.append([])
    #Se recorre cada columna de la fila, acorde a las ingresadas por el usuario
    while indice_columna<N:
        #El usuario ingresa el dato especificado
        dato_ingresado = eval(input("Ingresa el dato {} de la lista {}: "\
                .format(indice_columna+1,indice_fila+1)))
        #Se guarda el dato en la posicion correspondiente del arreglo
        matriz[indice_fila].append(dato_ingresado)
        indice_columna+=1
    else:
        #Reinicia el indice de columna
        indice_columna=0
    #Si existe otra fila, procede a repetir el codigo para ingresar sus datos
    indice_fila+=1
else:
    #Imprime la matriz
    for x in matriz :
        print(x)
    #Se muestra mensaje que acabo de imprimir la matriz
    print("Fin del arreglo")
