#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

adjetivo = ["roja", "grande", "dulce"]
frutas = ["manzana", "platano", "naranja"]

for x in adjetivo:
    for y in frutas:
        print(y,x)


