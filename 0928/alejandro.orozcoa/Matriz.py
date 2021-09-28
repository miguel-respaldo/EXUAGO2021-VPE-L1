#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or

filas = eval(input("Introduce numero de filas: "))
columnas = eval(input("Introduce numero de columnas: "))
matriz = []

for x in range(filas):
    matriz.append([])
    for y in range(columnas):
        valor = int(input("Ingresa Fila {}, Columna {}: ".format(x,y)))
        matriz[x].append(valor)

for x in matriz:
    print(x)


