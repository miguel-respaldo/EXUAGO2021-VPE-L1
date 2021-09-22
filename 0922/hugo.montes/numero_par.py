#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa para para determinar si el numero ingresado es par o impar
print("Identificacion de par o impar")

#se solicita el numero 
num = eval(input("ingresa tu dato"))

if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
