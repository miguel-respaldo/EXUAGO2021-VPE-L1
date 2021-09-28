#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later




m = int(input("ingresa cantidad de filas"))
n = int(input("ingresa cantidad de columnas"))
matriz =[]


for i in range(m):
    matriz.append([])
    for j in range(n):
        v = eval(input("Ingresa el valor "))
        matriz[i].append(v)

for x in matriz:
    print (x) 
