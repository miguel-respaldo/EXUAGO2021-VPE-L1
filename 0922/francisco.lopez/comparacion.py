#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Comparacion de dos numeros.
"""

#Entrada de datos
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero:"))

#Comparacion
if a==b:
    print("a y b son iguales")
elif a>b:
    print("a es mayor")
else:
    print("b es mayor")

