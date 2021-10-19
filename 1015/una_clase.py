#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Este es un modulo de ejemplo
de clases en python
"""

class MiClase:
    """
    Esta clase es de ejemplo
    """
    def __init__(self):
        self.prop1 = 4
        self.__prop2 = 5

    def metodos(self):
        """
        Este es un ejemplo dumy
        """
        return self.prop1 * self.__prop2

    def suma(self):
        """
        Este es un ejemplo dumy tambien
        """
        return self.prop1 + self.__prop2


objeto = MiClase()

print(objeto.prop1)
### print(objeto.__prop2)
