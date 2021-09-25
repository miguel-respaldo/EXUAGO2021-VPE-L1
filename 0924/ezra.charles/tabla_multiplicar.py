#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que imprime las tablas de multiplicar de un número dado por el usuario
"""

print("Programa que imprime las tablas de multiplicar de un número dado por el usuario")

# Pedir al usaurio el numero
numero = eval(input("Ingresa el numero: "))

# Impresion de tabla
for i in range(1, 11):
    print(numero, " x ", i, "=", i*numero)
    
