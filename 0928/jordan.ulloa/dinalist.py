#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que crea listas dinamicamente que ingresa el usuario

Hacer un programa que me llene una matriz nXm definica por el usuario
"""

#Se le desplegan mensajes de instruccion al usuario
print("Este programa crea una matriz de las dimensiones que usted requiera.")
print("Por favor ingresa el tamaño de la matriz que sera de nXm.")

#Se solicita el tamaño de la matriz de la matriz
n = int (input("Ingresa el valor de n: "))
m = int (input("Ingresa el valor de m: "))

#Se crea una matriz vacia
Matriz = []

#Se crean las matrices que seran de columnas
for x in range(n):
    Matriz.append([])

#Se ingresan los datos por el usuario
for x in range (n):
    for y in range (m):
        Matriz[x].append(eval(input(f"Ingresa el elemento {x}X{y}: ")))


#Se deplega la matriz final
for x in Matriz:
    print (x)
