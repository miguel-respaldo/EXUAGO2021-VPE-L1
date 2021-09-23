#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que detecta si un numero es par o impar.
Alba Castro y Jesus Apodaca
"""

#se piden el numero a evaluar
a = eval(input("Escribe un numero: "))

#se realiza la operacion de residuo para saber si es par o impar
if a % 2 == 0:
    print("El numero", a , "es par")
else:
    print("El numero {} es impar ".format(a))
