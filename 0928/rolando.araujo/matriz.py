#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que cree una matriz de n * m definida por el usuario
print("Matriz de n * m definida por usuario")

#Se piden los datos de la matriz
n = int(input("Definir valor de n: "))
m = int(input("Definir valor de m: "))

#Se crean los ciclos para agregar los valores a filas y columnas
n1 = []
n1.append([])

print("Valores de fila")
for x in range(n):
    numf = eval(input("Ingrese valor:" ))
    n1[0].append(numf)

m1 = []
m1.append([])

print("Valores de columna")
for y in range(m):
    numc = eval(input("Ingrese valor:" ))
    m1[0].append(numc)

print("La matriz que fue ingresada es la siguiente: ")
print(n1,m1)

