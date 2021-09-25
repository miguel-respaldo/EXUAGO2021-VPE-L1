#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
PROGRAMA QUE DETERMINA SI UN NÚMERO ES PAR O IMPAR
Cesar Alvarado y José Leonardo Quiñonez
"""
#Captura de numero
print("Programa que determina si un número es par o impar")
y = eval(input("Ingresa un número: "))

#Condiciones para determinar si el numero es par o impar
x = y % 2
if x == 0:
    print("El numero :" , y, " es par")
else:
    print("El numero :" , y, " es impar")
    
