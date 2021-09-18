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
    #Inicio de programa
    print("Programa para calcular el promedio de 5 números")
    """
    Se toman los numeros, el usuario los ingresa:
    """
    numero1=eval(input("Número 1: "))
    numero2=eval(input("Número 2: "))
    numero3=eval(input("Numero 3: "))
    numero4=eval(input("Numero 4: "))
    numero5=eval(input("Numero 5: "))
    """
    Se calcula el promedio 
    """
    promedio = (numero1+numero2+numero3)/5; 
    """Se imprime el promedio de salida para el usuario.
    """
    print("El promedio del numero fue: ", promedio)


if __name__ == "__main__":
    main()

