#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que permite llenar de manera dinamica una matriz

#entrada de valores del tamaño de la matriz
num_renglones = int(input("ingresa el numero de renglones "))
num_columnas = int(input("ingresa el numero de columnas "))

#Variable matriz vacia
matriz = []

#Ingreso de datos de uno en uno
for i in range(num_renglones):
    matriz.append([])
    for j in range(num_columnas):
        matriz[i].append(input("dato {},{} :".format( i, j)))

#impresion de la matriz
for renglon in range(num_renglones):
    print (matriz[renglon])

