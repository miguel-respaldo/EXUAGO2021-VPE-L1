#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Se pide al usuario que ingrese un numero
num = eval(input("Ingresa un numero te dire si es par o inpar:"))

#Se evalua si el numero es par o impar
print ("\nEs par" if num%2 == 0 else "\nEs Inpar")
