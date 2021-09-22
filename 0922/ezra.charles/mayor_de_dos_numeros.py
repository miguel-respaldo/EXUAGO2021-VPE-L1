#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que identifica al mayor de dos numeros dados por el usuario
"""

print("Programa para determinar el mayor de dos numeros")

# Pedir al usaurio dos numeros
numero1 = eval(input("Ingresa el primer numero: "))
numero2 = eval(input("Ingresa el segundo numero: "))

# Comparacion
if numero1 > numero2:
    print("El numero", numero1, "es mayor (el primero)")
elif numero1 < numero2:
    print("El numero", numero2, "es mayor (el segundo)")
else:
    print("Ambos numeros son iguales")
    

