#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

numero1 = eval(input("Ingresa un número 1: "))

print("el número que ingresaste fue", numero1)
print(type(numero1))

numero2 = eval(input("Ingresa un número2: "))

print("el número que ingresaste fue", numero2)
print(type(numero2))

numero3 = eval(input("Ingresa un número3: "))

print("el número que ingresaste fue", numero3, numero2, numero3)
print(type(numero3))

numero4 = eval(input("Ingresa un número4: "))

print("el número que ingresaste fue", numero4)
print(type(numero4))

numero5 = eval(input("Ingresa un número5: "))

print("el número que ingresaste fue", numero5)
print(type(numero5))


print("promedio de los 5",(numero1 + numero2 + numero3 + numero4 + numero5)/5)

