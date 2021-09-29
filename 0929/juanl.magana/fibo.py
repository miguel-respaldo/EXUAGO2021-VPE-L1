#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""
def fibo(numero):
    last = 1
    pen = 0
    for i in range(numero+1):
        if i == 0:
            res = 0
            continue
        elif i == 1:
            res = 1
            continue
        res = last + pen
        pen = last
        last = res
    return res

def main():
    n = int(input("Ingrese la posicion a consultar de la sucesion fibonacci "))
    res = fibo(n)
    print(f"El valor para la posicion {n} es {res}")

if __name__ == "__main__":
    main()

