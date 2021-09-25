#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
El siguiente programa imprime las tablas del 1 al 10, dependiento la que elija
el usuario.

Alba Gpe. Castro Melgoza
"""

#se pide la tabla a imprimir
tabla = int(input("Escribe el numero de la tabla que deseas que se imprima, del 1 al 10 "))
if tabla < 11:
    for num in range(11):
       print(num, "x", tabla, "=", (num*tabla))

else:
    print("Tabla incorrecta")

#se imprime la tabla
