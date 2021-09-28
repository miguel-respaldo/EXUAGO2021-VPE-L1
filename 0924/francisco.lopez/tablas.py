#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Tablas de multiplicar.
"""
#Ingreso de tabla a multiplicar.
t = int(input("Ingresa tabla a imprimir: "))

#Multiplicacion e imprsion de resultado.
for x in range(1,11):
    print(t, " x ",x, " = ",t*x) 
