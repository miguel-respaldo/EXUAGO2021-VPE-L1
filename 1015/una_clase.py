#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

class MiClase:
    prop1 = 4
    __prop2 = 5


objeto = MiClase()

print(objeto.prop1)
print(objeto.__prop2)

