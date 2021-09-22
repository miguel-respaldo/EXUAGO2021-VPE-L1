#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Hacer un programa que pida 2 numeros y me diga cual es el mayor
print("Programa para determinar cual de dos numeros es mayor o si son iguales")

#Se piden los numeros
numero1 = eval(input("Ingresa numero 1:"))
numero2 = eval(input("Ingresa numero 2:"))

#Se realizan las comparaciones para definir cual numero es mayor
if numero1 > numero2: print("El mayor es:", numero1)
elif numero1 == numero2: print("Ambos numeros son iguales",)
else: print("El mayor es:", numero2)
