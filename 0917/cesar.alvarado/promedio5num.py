#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa para calcular el promedio
de 5 numeros ingresados por el usuario
"""

#Ingresamos cinco numeros y se guardan en 5 variables
num1=eval(input("Ingrese 1er numero: "))
num2=eval(input("Ingrese 2do numero: "))
num3=eval(input("Ingrese 3er numero: "))
num4=eval(input("Ingrese 4to numero: "))
num5=eval(input("Ingrese 5to numero: "))
#se realiza la suma de todos y la division entre el total de elementos
res = (num1+num2+num3+num4+num5)/5    
#Se imprime el resultado
print("El promedio es: ",res)

