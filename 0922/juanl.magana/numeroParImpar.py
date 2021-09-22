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
    #Lectura del numero 
    a=eval(input("Ingrese numero "))
    #Condicional que arroja si es numero par e impar
    if a%2==0:
        print("El numero es par")
    else:
        print("El numero es impar")
    


if __name__ == "__main__":
    main()

