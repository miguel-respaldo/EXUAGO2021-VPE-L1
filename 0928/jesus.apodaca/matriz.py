#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que captura los elementos de la matriz con dimension dado por el usuario AxB  

print ("ingese las dimensienes de la matriz a capturar")
m = int(input("ingresa cantidad de filas"))
n = int(input("ingresa cantidad de columnas"))
#se capturar las dimensiones que tendra la matriz y se inicializa
matriz =[]

#utiliza ciclos anidados para hacer el llenado de las matrices filaxcolumna 
for i in range(m):
    matriz.append([])
    for j in range(n):
        v = eval(input("Ingresa el valor "))
        matriz[i].append(v)

#imprime el valor de la matriz para visualizacion del usario
for x in matriz:
    print (x)
~                                   
