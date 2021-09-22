#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


x = 50

if x > 10:
    print("Es mayor a diez,")
    if x > 20:
        print("Es mayor a veinte")
    else:
        print("Es menor a veinte")

print("-------------")

if x > 10:
    print("es mayor a diez,".upper())
elif x > 20:
    print("Es mayor a veinte".upper())
else:
    print("Es menor a veinte".upper())

"""
switch (x) {
case >10:
case >20:
default:
}
"""


