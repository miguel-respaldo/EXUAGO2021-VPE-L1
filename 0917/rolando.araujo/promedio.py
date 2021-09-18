#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

print("Ingresa 5 numeros")

numero1 = eval(input("Ingresa numero: "))
numero2 = eval(input("Ingresa numero: "))
numero3 = eval(input("Ingresa numero: "))
numero4 = eval(input("Ingresa numero: "))
numero5 = eval(input("Ingresa numero: "))

promedio = ((numero1 + numero2 + numero3 + numero4 + numero5) / 5 )
print("el promedio es", promedio)
