#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Author: Moisés Emmanuel Pérez Ramos
# Fecha: 
"""
Programa para determinar si un numero es par o impar
"""

def main():
    """
    Inicio del programa
    """
    print("*Cálculo de par o impar**")
    num=eval(input("Ingrese un número: ")) 
    #condicion if 
    print("El numero ", num , " es un número par") if num%2 == 0 else print("El numero ", num, " es un número impar")


if __name__ == "__main__":
    main()

