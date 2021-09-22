#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que indica cual de dos numeros es mayor
print("Comparador de dos numeros\n")

#Entrada por partde del usuario de los numeros a comparar
num1 = eval(input("Ingresa el valor de a: "))
num2 = eval(input("Ingresa el valor de b: "))

#Comparacion e impresion segun el caso (a>b, b>a o a=b)
if num1 > num2: print("a es mayor que b")
elif num1 < num2: print("b  es mayor que a")
else: print("a y b son iguales")
