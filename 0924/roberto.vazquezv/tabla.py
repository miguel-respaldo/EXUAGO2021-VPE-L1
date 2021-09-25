#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que calcula la tabla de multiplicar (1-10) de un numero dado

#Entrada de la tabla seleccionada por el usuario
num = int(input("Ingresa la tabla a calcular: "))

#Variable multiplicador
mult = 1

#Imprime el resultado y se detiene cuando el multiplicador pasa de 10
while mult < 11:
    print("{} x {} = {}".format(num, mult, num * mult))
    mult += 1
