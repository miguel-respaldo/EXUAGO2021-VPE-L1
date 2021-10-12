#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo programa principal y funciones
"""
import funciones

def main():
    """
    Comentario de la función
    """
    print("Programa principal")
    print("La suma", funciones.suma(2,3))
    print("La resta", funciones.resta(6,3))
    res = funciones.multiplicacion(2,2)
    print(f"La multiplicaciones {res}")


if __name__ == "__main__":
    main()

