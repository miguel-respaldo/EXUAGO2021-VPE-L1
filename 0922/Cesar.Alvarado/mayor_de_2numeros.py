#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que indica cual numero es mayor 
de dos numeros ingresados por el usuario
"""
#Solicitamos los numeros al usuario
num1 = eval(input("Ingrese el primer numero: "))
num2 = eval(input("Ingrese el segundo numero: "))

#Realizamos la comparacion y desplegamos resultado al usuario
if num1>num2:
    print("El primer numero es mayor al segundo.")
elif num1<num2:
    print("El segundo numero es mayor al primero")
else:
    print("El primer numero y el segundo son iguales")
