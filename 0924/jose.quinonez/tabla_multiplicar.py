#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
PROGRAMA QUE CALCULA UNA TABLA DE MULTIPLICAR 
"""
#PREGUNTAR DE CUAL NUMERO QUIERE LA TABLA DE MULTIPLICAR
print("Bienvenido al programa que calcula la tabla de multiplicar de un número  dado")
x = int(input(" Ingresa el numero:"))

#CALCULAR E IMPRIMIR LAS TABLA
for y in range(1,11):
    print(x,"x",y,"=",x*y)

