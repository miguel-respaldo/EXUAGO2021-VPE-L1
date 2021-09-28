#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Se explica el programa y se piden la dimenciones de la matriz
print("El programa crea una matriz de con el numero de filas y columnas que tu requieras")
fila = int(input("Ingrese el numero de filas:"))
columna = int(input("Ingrese el numero de columnas:"))

#Se crea una nueva matrix 
matriz  = []
for i in range(fila):
    matriz.append([])

#Se ingresan y se guardan los datos para llenar la matriz
for i in range(fila):
    for x in range(columna):
        matriz[i].append(input("Ingrese datos:"))

#Se imprime la matriz 
for i in range(fila):
    print(matriz[i])
