#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa para calcular el promedio de 5 numeros
ingresados por el usuario
"""
print("|Ingrese 5 numeros para calcular el promedio|")

#Captura de los 5 numeros
num1 = eval(input("Ingresa el primer numero: "))
num2 = eval(input("Ingresa el segundo numero: "))
num3 = eval(input("Ingresa el tercer numero: "))
num4 = eval(input("Ingresa el cuarto numero: "))
num5 = eval(input("Ingresa el quinto numero: "))

#Se obtiene el promedio 
resultado = (num1+num2+num3+num4+num5)/5

#Se imprime en pantalla el resultado
print("El promedio de sus numeros es: ", resultado)
