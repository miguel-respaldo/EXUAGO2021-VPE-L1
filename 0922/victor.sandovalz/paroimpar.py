#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


#Solicitar numero al usuario
a = int(input("Ingresa un numero: "))

#Codigo que calcula el modulo de cualquier numero
if a % 2 != 0:
    print("El numero es impar")
else:
    print("El numero es par")

