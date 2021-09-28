#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Este programa crea una lista de tamnio y elementos definidos por el usuario.
Jose.Quinionez
Cesar.Alvarado
"""
#Explicacion de programa al usuario
print("Este programa crea una lista de tamanio y elementos definidos por el usuario")
#Se ingresa dimensiones de matriz
F = int(input("Ingrese el tamanio de filas: "))
C = int(input("Ingrese el tamanio de columnas: "))
#Se crea matriz vaci
matriz = []
#Se rellena matriz de ceros
for x in range(F):
    matriz.append([0]*C)
#Se realiza el llenado con for anidados
for x in range(F):
    for y in range(C):
        matriz[x][y] = eval(input("ingrese elemento[{}][{}]: ".format(x,y)))
#Se imprime matriz
print(matriz)
