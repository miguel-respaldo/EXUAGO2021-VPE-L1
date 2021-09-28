#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que permite llenar dinamicamente una matriz NxM

#Entrada de valores de tamaño de la matriz
n = int(input("Numero de renglones: "))
m = int(input("Numero de columnas: "))

#Variable matriz vacia
matriz = []

#Entrada de elementos (uno por uno)  de la matriz
for i in range(n):
    matriz.append([])
    for j in range(m):
        matriz[i].append(input("Ingresa valor de [{},{}]: ".format(i,j)))

print("Matriz final")

#Impresion de la matriz en forma dimensional
for line in range(n): 
    print(matriz[line])



