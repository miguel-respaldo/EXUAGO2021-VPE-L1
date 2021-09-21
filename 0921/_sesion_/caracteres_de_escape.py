#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
import time

txt = "Esta es una linea\nesta es otra linea"
print("1: " + txt)
txt = "Esta es una linea 1234567890abcdefg\resta es otra linea jajaja"
print("2: " + txt)
txt = "Esta es una linea\ttabulador\ttab\ttab"
print("3: " + txt)


for i in range(10,-1,-1):
    print(i,end="")
    time.sleep(1)
    print("   \r",end="")
