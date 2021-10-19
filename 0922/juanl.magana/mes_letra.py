#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
from ast import literal_eval
def main():
    """
    Funcion main para la conversion de numero de mes a nombre del mes
    """
    #Lectura del numero del mes
    mes = literal_eval(input("Ingrese el numero del mes\n"))

    #Impresion en letra del mes
    if mes == 1:
        print("el mes es Enero")
    elif mes == 2:
        print("el mes es Febrero")
    elif mes == 3:
        print("el mes es Marzo")
    elif mes == 4:
        print("el mes es Abril")
    elif mes == 5:
        print("el mes es Mayo")
    elif mes == 6:
        print("el mes es Junio")
    elif mes == 7:
        print("el mes es Julio")
    elif mes == 8:
        print("el mes es Agosto")
    elif mes == 9:
        print("el mes es Septiembre")
    elif mes == 10:
        print("el mes es Octubre")
    elif mes == 11:
        print("el mes es Noviembre")
    elif mes == 12:
        print("el mes es Diciembre")
    #else: print("Error: Introduce un valor entre 1 y 12")



if __name__ == "__main__":
    main()
