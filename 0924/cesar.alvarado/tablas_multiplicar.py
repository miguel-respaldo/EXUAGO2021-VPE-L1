#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Este programa pide un numero del 1-10 al usuario
y posteriormente desplega la tabla de multiplicar
correspondiente
"""
print("Este programa despliega tablas de multiplicar del 1 al 10\n")
init = 1
end = 10
opcion = eval(input("Que tabla de multiplicar desea consultar?"))
count = 1

if opcion <=10 and opcion >0:
    for i in range(init,end+1):
        res = opcion * i
        print(opcion,"X",i,"=",res)
else:
    print("Esa opcion no esta implementada aun...")

