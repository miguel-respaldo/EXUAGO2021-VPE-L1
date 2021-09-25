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
    #Informamos el proposito del programa
    print("A continuacion ingresa la tabla a calcular")
    #Leemos el valor ingresado por el usuario
    tabla = eval(input(""))
    #calculamos iterando con un for desde 0 hasta a 10
    for i in range(11):
        #calculo del resultado
        res = tabla*i
        #imprimimos el resultado
        print(f"{tabla} x {i} = {res}")

if __name__ == "__main__":
    main()

