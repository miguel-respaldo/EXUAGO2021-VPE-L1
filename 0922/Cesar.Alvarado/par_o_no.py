#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que determina si un numero ingresado
por el usuario es par o impar
"""
#Mensaje de info al usuario
print("<<<Hola este programa determina si un numero es par o no>>>")
#Pedimos el numero al usuario
num = eval(input("Ingrese un numero: "))
#Evaluacion del numero y desplegue de resultado
if num%2 != 0: print("Tu numero",num," es impar")
else: print("Tu numero",num," es par")

"""
C.Alvarado
"""
