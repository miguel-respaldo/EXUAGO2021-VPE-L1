#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

class MiClase:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.__num2 = num2

    def miMetodo(self):
        print("La suma de los numeros es: ", self.num1 + self.__num2)


objeto = MiClase(3.1416, 2.17)

print(objeto.num1)
##print(objeto.__num2)

objeto.miMetodo()

