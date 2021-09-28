#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Imprimir una matriz de NxM.
"""

#Entrada de datos.
fila = int(input("Ingresa la cantidad de filas: "))
columna = int(input("Ingresa la cantidad de columnas: "))

#Declaracion de lista.
matriz =[] 

#Creacion matriz agregando N listas dentro de matriz.
for c in range(columna):
    matriz.append([])

#Captura de elementos en cada posicion de la matriz.
for c in range(columna):
    for f in range(fila):
       matriz[c].append(eval(input(f"Ingresa el elemento {c},{f}:")))

#Impresion de resultado.
x = 0
print("\nMatriz:")
while x < fila:
    print(matriz[x])
    x += 1
