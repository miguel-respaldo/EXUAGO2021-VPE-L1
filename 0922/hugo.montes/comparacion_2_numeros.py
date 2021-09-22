#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#programa que pida 2 numeros y me diga cual es el mayor
print("Comparación de 2 numeros")

#se solicitan 2 datos y se guardan
num_1 = eval(input("ingrese el primer numero"))
num_2 = eval(input("ingrese el segundo numero"))

#condicion para imprimer el primer dato 
if num_1 > num_2: print("el primer numero es mayor ")

#condicion para imprimir el segundo dato
elif num_1 < num_2: print("el segundo numero es mayor ")

#en caso de que ambos datos sean iguales
else: print("ambos numeros ingresados son identicos ")
