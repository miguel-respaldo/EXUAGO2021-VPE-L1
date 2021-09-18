#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#PROGRAMA PARA CALCULAR EL PROMEDIO DE 5 NUMEROS INTRODUCIDO POR EL USUARIO

# Se solicitan los 5 numeros uno por uno
numero1 = eval(input("Ingresa el número 1: "))
numero2 = eval(input("Ingresa el número 2: "))
numero3 = eval(input("Ingresa el numero 3: "))
numero4 = eval(input("Ingresa el numero 4: "))
numero5 = eval(input("Ingresa el numero 5: "))

# Se calcula el promedio con la suma de los numeros y, como se solicitan 5,
# se divide al final entre 5

promedio = (numero1 + numero2 + numero3 + numero4 + numero5)/5
print("el número que ingresaste fue", promedio)
