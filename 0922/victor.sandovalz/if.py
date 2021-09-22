#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

a = int(input("Ingresa numero a: "))
b = int(input("Ingresa numero b: "))

if (a>b):
    print("a es mayor que b")
else:
    if (a==b):
        print("a es igual a b")
    else: 
        print("b es mayor que a")

