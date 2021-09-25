#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Author: Moisés Emmanuel Pérez Ramos
# Fecha: 
"""
Programa para determinar tablas de multiplicar
"""

def main():
    """
    Breve descripcion para el usuario
    """
    print("***Programa para calcular la multiplicación de numeros del 1 al 10***")
    num1 = int(input("Ingresa el numero del cual deseas la multiplicación:"))
    
    num2=[1,2,3,4,5,6,7,8,9,10]

    for i in num2:
        res = num1 * i
        print(num1, " x ", i ," = ", res)


if __name__ == "__main__":
    main()

