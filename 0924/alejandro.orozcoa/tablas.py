#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Se pide al usuario ingresare el numero de la tabla de multiplicar
num = eval(input("Ingresa la tabla a imprimir: "))

#Con un ciclo for recorro del 0 al 10 multiplico el numero ingresado
for i in range(1,11):
    result = i * num
    print(num,"*",i,"=",result)
