#!/usr/bin/env python3
# c-basic-offset: 4; tab-widht: 8; indent-tabs-mode: nil
#vi: set shiftwidth=4 tabstop=8 expandtab:
#indentSize=4;tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or later

#tabla de multiplicar
 
tablamul = eval(input("ingresa el valor de la tabla a imprimir"))
num = 1 

while num < 11:
	 
	print("{} x {} = {}".format(tablamul, num, tablamul*num))
	num += 1
