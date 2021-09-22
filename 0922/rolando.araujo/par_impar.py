#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que define si un numero es par o impar
print("Programa que pide un numero y define si es par o impar")

#Se pide el numero
numero = eval(input("Ingres el numero :"))

#Se verifica si el numero es par o impar
if (numero % 2) == 0: print("El numero es par")
else: print("El numero es impar")
