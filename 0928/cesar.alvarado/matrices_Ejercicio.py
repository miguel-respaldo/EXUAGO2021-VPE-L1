#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Matriz NxM definida por el usuario
Jose.Quiñonez
Cesar.Alvarado
"""
#Ingreso de datos
N = int(input("Ingrese el tamaño N de la matriz: "))
M = int(input("Ingrese el tamaño M de la matriz: "))
#Matriz vacia
Matriz = []

#Se construye la matriz
for x in range(N):
    Matriz.append([0]*M)
#Se empieza a llenar la matriz de NxM
for x in range(N):
    for y in range(M):
        Matriz[x][y] = eval(input("ingresa dato: "))
#Se imprime matriz
print(Matriz)        
