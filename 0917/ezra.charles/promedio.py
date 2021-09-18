#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Promedio de 5 numeros 
By EzraCharles
"""

def main():
    """
    Comentario de la función
    """
    numero1 = eval(input("Ingresa el primer número: "))
    numero2 = eval(input("Ingresa el segundo número: "))
    numero3 = eval(input("Ingresa el tercer número: "))
    numero4 = eval(input("Ingresa el cuarto número: "))
    numero5 = eval(input("Ingresa el quinto número: "))

    promedio = (numero1 + numero2 + numero3 + numero4 + numero5) / 5 
    print("El promedio de los números que ingresaste es", promedio)


if __name__ == "__main__":
    main()

