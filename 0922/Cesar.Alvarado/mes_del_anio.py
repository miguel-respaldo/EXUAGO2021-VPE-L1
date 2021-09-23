#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Este programa te dice que mes es a partir del numero ingresado
L. FRANCISCO
C.ALVARADO
"""

print("Este programa indica que mes al digitar su numero")
mes = eval(input("Ingrese el numero del mes de 1 a 12: "))
if mes == 1: print("Su numero",mes,"corresponde a Enero")
elif mes == 2: print("Su numero",mes,"corresponde a Febrero")
elif mes == 3: print("Su numero",mes,"corresponde a Marzo")
elif mes == 4: print("Su numero",mes,"corresponde a Abril")
elif mes == 5: print("Su numero",mes,"corresponde a Mayo")
elif mes == 6: print("Su numero",mes,"corresponde a Junio")
elif mes == 7: print("Su numero",mes,"corresponde a Julio")
elif mes == 8: print("Su numero",mes,"corresponde a Agosto")
elif mes == 9: print("Su numero",mes,"corresponde a Septiembre")
elif mes == 10: print("Su numero",mes,"corresponde a Octubre")
elif mes == 11: print("Su numero",mes,"corresponde a Noviembre")
elif mes == 12: print("Su numero",mes,"corresponde a Diciembre")
else: print("Ingrece un numero del 1 al 12")
