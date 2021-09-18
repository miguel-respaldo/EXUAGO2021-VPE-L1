#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

'''
Ejercicio de clase donde se pide ingresar 5 numeros y se ingresa
el promedio de dichos numeros.
'''

#Se despliega un mensaje de instruccion.
print("Programa que obtiene el promedio de 5 numeros")
print("Ingrese 5 numeros")

#Se solicitan los 5 numeros mencionados anteriormente.
a = eval(input("Ingrese a: "))
b = eval(input("Ingrese b: "))
c = eval(input("Ingrese c: "))
d = eval(input("Ingrese d: "))
e = eval(input("Ingrese e: "))

#Se realiza el promedio de los 5 numeros a su vez que se despliegan
print((a+b+c+d+e)/5)
