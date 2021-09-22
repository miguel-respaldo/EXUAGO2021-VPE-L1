#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Se Piden los numeros a evaluar
num1 = eval(input("Ingresa un numero: "))
num2 = eval(input("Ingresa otro numero:"))

#Se valuan las variables
if num1 > num2:
    print("A es mayor que B" )
elif num1 < num2:
    print("B es mayor que A")
else:
    print("Son iguales")
