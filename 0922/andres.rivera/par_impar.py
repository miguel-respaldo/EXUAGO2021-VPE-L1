#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que identifique si un numero es par o impar
"""

print("Programa para determinar si un numero es par o impar")

# Pedir numero al usuario
numero = eval(input("Ingresa el numero: "))

# Comparacion
if numero % 2 == 0:
    print("El numero", numero, "es un numero par")
else:
    print("El numero", numero, "es un numero impar")