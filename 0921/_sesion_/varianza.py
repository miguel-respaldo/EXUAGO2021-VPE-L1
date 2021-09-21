#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

num1 = eval(input("Escribe el numero 1: "))
num2 = eval(input("Escribe el numero 2: "))
num3 = eval(input("Escribe el numero 3: "))
num4 = eval(input("Escribe el numero 4: "))
num5 = eval(input("Escribe el numero 5: "))

promedio = (num1 + num2 + num3 + num4 + num5)/5
varianza = ((num1 - promedio)**2 + (num2 - promedio)**2 + (num3 - promedio)**2 + (num4 - promedio)**2 +(num5 - promedio)**2) / (5-1)

print("La varianza es: ", varianza)
