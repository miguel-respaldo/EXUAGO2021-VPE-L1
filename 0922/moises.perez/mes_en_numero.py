#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# Author: Moisés Emmanuel Pérez Ramos
# Fecha: 
"""
Programa para conocer el nombre de un mes, dado el numero de mes
"""

def main():
    """
    Presentacion del programa para el usuario.
    Ingreso de numero por el usuario
    """
    print("**Programa para determinar el nombre de un mes, por su número**")
    nmes = int(input("Número de mes: "))
    if nmes == 1: 
        print("Enero")
    elif nmes == 2:
        print("Febrero")
    elif nmes == 3: 
        print("Marzo")
    elif nmes == 4: 
        print("Abril")
    elif nmes == 5:
        print("Mayo")
    elif nmes == 6: 
        print("Junio")
    elif nmes == 7:
        print("Julio")
    elif nmes == 8:
        print("Agosto")
    elif nmes == 9:
        print("Septiembre")
    elif nmes == 10: 
        print("Octubre")
    elif nmes == 11:
        print("Noviembre")
    elif nmes == 12:
        print("Diciembre")
    else: 
        print("El numero no pertenece a un número de mes ")
    #Fin de programa

if __name__ == "__main__":
    main()

