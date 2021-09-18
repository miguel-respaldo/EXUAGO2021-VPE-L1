#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

A = eval(input("Ingresa el primer numero: "))
B = eval(input("Ingresa el segundo numero "))
C = eval(input("Ingresa el tercer numero "))
D = eval(input("Ingresa el cuarto numero "))
E = eval(input("Ingresa el quinto numero "))
prom = (A+B+C+D+E)/5
print("el promedio de los numeros es", prom)
print("El tipo de dato es: ",(type(prom)))
