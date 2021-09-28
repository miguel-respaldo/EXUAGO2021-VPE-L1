#!/usr/bin/env python3

# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

filas = eval(input("Ingrese el número de lineas que desea para su matriz: "))
columnas = eval(input("Ingrese el número de columnas que desea para su matriz: "))
matriz = []

for x in range(filas):
	matriz.append([])
	for y in range(columnas):	
		valor = int(input("Ingresa fila {}, columna {}: ".format(x,y)))
		matriz[x].append(valor)
for x in matriz:
	print(x)



