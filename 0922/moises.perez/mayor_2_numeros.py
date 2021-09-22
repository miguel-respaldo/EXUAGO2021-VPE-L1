#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Author: Moisés Emmanuel Pérez Ramos
# Fecha: 22/09/2021
"""
Programa para determinar el mayor de 2 numeros
"""

def main():
    """
    Comentario de la función
    """
    print("***Programa para determinar el mayor de dos números***")
    num1 = eval(input("Ingresa numero 1: "))
    num2 = eval(input("Ingresa numero 2: "))

    if num1 > num2: 
        print("El numero mayor es : ", num1)
    elif num2<num1: 
        print("El numero mayor es : ", num2)
    elif num1==num2:
        print("Ambos numeros son iguales")
    else: 
        print("No se ingresaron numeros")

if __name__ == "__main__":
    main()

