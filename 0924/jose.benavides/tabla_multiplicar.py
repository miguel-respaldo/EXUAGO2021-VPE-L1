#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

num =  eval(input("Ingresa un numero y te regresare su tabla de multiplicar: "))

for i in range(1,11):
    print(i,"*",num, " = ",i*num)
