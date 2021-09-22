#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

print("Programa que compara dos numeros")
a = eval(input("a = "))
b = eval(input("b = "))

if a < b: print("b es mayor que a.")
elif a == b: print("a y b son iguales.")
else: print("a es mayor que b.")


