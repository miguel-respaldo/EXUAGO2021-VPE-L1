#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def fibonacci(num):
    if num <= 2:
        num = 1
    
    else:
        num = fibonacci(num - 1) + fibonacci(num - 2)

    return num

def main():
    numero = int(input("Escribe el numero a calacular de la serie de fibonacci:  "))
    if numero < 1:
        print("chale krnal eso no te lo venimos manejando")
    else:
        print("la posicion {} de la serie de fibonacci es: {}".format(numero,fibonacci(numero)))

if __name__=="__main__":
    main()
