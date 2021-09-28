#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejercicio que llena una matriz de NxM definida por el usuario
Rolando Araujo y Alba Castro
"""
print("Matriz de n*m definida por el usuario")

#se piden los datos de la matriz al usuario
n = int(input("Ingresa el valor de n, filas: "))
m = int(input("Ingresa el valor de m, columnas: "))

#se crean los ciclos para agregar los valores de las filas y columnas dependiendo los valores que va ingresando el usuario
n1 = []
n1.append([])

print("Valores de fila")

for x in range(n):
    numf = eval(input("Ingrese valor: "))
    n1[0].append(numf)

m1 = []
m1.append([])
print("Valores de columnas")
for y in range(m):
    numc = eval(input("Ingrese valor: "))
    m1[0].append(numc)

print("La matriz que fue ingresada es la siguiente: ")
print(n1, m1)

