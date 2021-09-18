#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
#Programa para sacar el promedio de 5 numeros
print("Promedio de 5 numeros")

#se solicitan 5 numeros para sacar el promedio 
num = eval(input("ingresa el primer numero: "))
num1 = eval(input("ingresa el segundo numero: "))
num2 = eval(input("ingresa el tercer numero: "))
num3 = eval(input("ingresa el cuarto numero: "))
num4 = eval(input("ingresa el quinto numero: "))

#se imprime mientras realiza la operación para sacar el promedio
print("el promedio del numero es",(num + num1 + num2 + num3 + num4)/5 )

