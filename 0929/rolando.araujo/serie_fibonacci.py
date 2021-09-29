#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def calculo(n):

    if n == 0:
        return 0
    elif n ==1 or n ==2:
        return 1
    else:
        return calculo(n-1) + calculo(n-2)
def main():  
    
    n = int(input("Ingresa el numero: "))

    print(calculo(n))


if __name__ == "__main__":
    main()

