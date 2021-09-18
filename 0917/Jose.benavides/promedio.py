#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-lat

#Se piden los datos al usuario
n1 = eval(input("Ingrese una calificacion: "))
n2 = eval(input("Ingrese segunda calificaion: "))
n3 = eval(input("Ingrese tercera calidicacion: "))
n4 = eval(input("Ingrese cuarta calificacion: "))
n5 = eval(input("Ingrese quinta calificacion: "))

#Se imprime el promedio de los datos ingresados
print("El promedio es:",((n1+n2+n3+n4+n5)/5))
