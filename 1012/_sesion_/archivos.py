#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

def main():
    """
    Comentario de la función
    """
    file = open("archivo.txt","r")

    for linea in file:
        print(linea, end="")

    # regresamos al principio del archivo
    file.seek(0)

    for linea in file:
        print(linea, end="")


if __name__ == "__main__":
    main()

