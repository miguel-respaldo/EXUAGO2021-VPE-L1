#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que llena una matriz de NxM definida por el usuario
"""

print("Programa que llena una matriz de NxM definida por el usuario")

matriz = []

# Pedir tamanio de matriz al usuario NxM
tamanio_N = int(input("Ingresa el numero N (renglones): "))
tamanio_M = int(input("Ingresa el numero M (columnas): "))

# Pedir al usuario contenido de matriz
for i in range(tamanio_N):
    matriz.append([])
    for j in range(tamanio_M):
        matriz[i].append(input("Ingresa elemento de [{}, {}]: ".format(i,j)))

# Impresion de matriz en forma de lista
#print(matriz)

# Imprimir de matriz en forma dimensional
print("Matriz dada: ")
for line in range(tamanio_N):
    print(matriz[line])