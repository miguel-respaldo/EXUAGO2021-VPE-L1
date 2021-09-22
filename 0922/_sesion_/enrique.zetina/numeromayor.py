#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


A = eval(input("Ingresa el numero correspondiente a A: "))
B = eval(input("Ingresa el numero correspondiente a B: "))

if A>B: print("El primer numero es el mayor: \n",A)
elif A<B: print("El segundo numero es mayor: \n",B)
else: print("son iguales",A)
