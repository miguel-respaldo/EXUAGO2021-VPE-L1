#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

f = open("demo2.txt","a")
f.write("Ahora el archivo tiene mas contenido!")
f.close()

f = open("demo2.txt","r")
print(f.read())

