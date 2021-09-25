#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


A = eval(input("que tabla quieres? "))


for i in range(1,11):
    x=(A*i)
    print(A,"por",i,"Ess igual a ",x)
    i+= 1
