#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que regresa el numero de la posicion n de la secuencia de fibonacci

#Se declara la función donde se calculará la serie de fibonacci
def calculo(n):
    if n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return calculo(n-1) + calculo(n-2)

#Se pide el numero y se imprime esa posición
def main():
    n = int(input("Ingrese posicion: "))

    print(calculo(n))


if __name__ == "__main__":
    main()

