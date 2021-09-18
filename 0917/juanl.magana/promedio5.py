#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

def main():
    """
    Comentario de la función
    """
    suma = 0 """Se inicilaiza variable suma"""
    print("Calculador de promedio de 5 numeros")"""Se muestra al usuario el
    proposito del programa"""
    for i in range(5):"""Ciclo for para realizar la suma de los enteros
    ingresados por el usario"""
        suma+=eval(input(f"Ingrese numero entero # {i+1}\n"))"""Se imprime y se
        recibe el numero ingresado por el usuario"""
    promedio=suma/5"""Se finaliza el for y se obtiene el promedio"""
    print("El promedio es ",promedio)"""Se obtiene el promedio"""


if __name__ == "__main__":
    main()

