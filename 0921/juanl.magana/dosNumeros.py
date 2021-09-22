#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

def main():
    print("Ingrese dos numeros para saber cual es el mayor\n")
    a=eval(input("Ingrese primer numero: \n "))
    b=eval(input("Ingrese segundo  numero: \n "))
    if a>b:
        print(f"{a} es el numero mayor")
    elif b>a:
        print(f"{b} es el numero mayor")

if __name__ == "__main__":
    main()

