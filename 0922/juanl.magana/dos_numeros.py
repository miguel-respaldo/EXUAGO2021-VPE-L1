#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Programa que calcula el mayor de dos numeros
"""
from ast import literal_eval
def main():
    """
    Funcion principal que calcula el mayor de dos numeros
    """
    #Informa al usuario el objetivo del programa
    print("Ingrese dos numeros para saber cual es el mayor")
    #lectura de dos numeros
    primer_numero = literal_eval(input("Ingrese primer numero: \n"))
    segundo_numero = literal_eval(input("Ingrese segundo  numero: \n"))
    #condicional para calcular el numero mayor y su posterior impresion
    if primer_numero > segundo_numero:
        print(f"{primer_numero} es el numero mayor")
    elif segundo_numero > primer_numero:
        print(f"{segundo_numero} es el numero mayor")
    else:
        print("Ambos numeros son iguales")

if __name__ == "__main__":
    main()
