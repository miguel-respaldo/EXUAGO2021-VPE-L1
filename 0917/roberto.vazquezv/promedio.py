#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que calcula la media/promedio de 5 numeros
print("Calculadora de promedio de 5 numeros\n")

#Entrada de los 5 numeros por parte del usuario
num1 = eval(input("Ingresa el primer numero:  "))
num2 = eval(input("Ingresa el segundo numero: "))
num3 = eval(input("Ingresa el tercer numero: "))
num4 = eval(input("Ingresa el cuarto numero: "))
num5 = eval(input("Ingresa el quinto numero: "))

#Calcula e imprime el resultado empleando X = (x1 +...xn)/n
print("El promedio es:", (num1 + num2 + num3 + num4 + num5) / 5)
