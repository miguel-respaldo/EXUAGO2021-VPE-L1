#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que pide dos numeros y muestra cual de ellos es el mayor o iguales
# Alba Gpe. Castro Melgoza

#se piden al usuario los numeros a evaluar
num1 = eval(input("Ingrese el primer numero: "))
num2 = eval(input("Ingrese el segundo numero: "))

#se evaluan y se imprimen
if num1 > num2: print("El primer numero es mayor: ", num1)

elif num2 > num1: print("El segundo numero es mayor: ", num2)

else: print("Los numeros son iguales")
