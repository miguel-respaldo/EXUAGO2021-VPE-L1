#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

import math

a = eval(input("Escribe el valor de a: ")
b = eval(input("Escribe el valor de b: ")
c = eval(input("Escribe el valor de c: ")

discriminante = b**2 - 4*a*c

x1 = (-b + math.sqrt(discriminante)) / (2*a)
x2 = (-b - math.sqrt(discriminante)) / (2*a)

print("x1 = ", x1)
print("x2 = ", x2)
