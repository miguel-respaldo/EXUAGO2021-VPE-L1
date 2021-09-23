#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que indica el nombre del mes al ingresa su numero
mes = eval(input("Ingresa el numero del mes (1-12): "))

#Casos del 1 al 12 (enero - diciembre)
if mes == 1: print("El mes es enero")
elif mes == 2: print("El mes es febrero")
elif mes == 3: print("El mes es marzo")
elif mes == 4: print("El mes es abril")
elif mes == 5: print("El mes es mayo")
elif mes == 6: print("El mes es junio")
elif mes == 7: print("El mes es julio")
elif mes == 8: print("El mes es agosto")
elif mes == 9: print("El mes es septiembre")
elif mes == 10: print("El mes es octubre")
elif mes == 11: print("El mes es noviembre")
elif mes == 12: print("El mes es diciembre")
elif mes <= 0 or mes > 12: print("Numero no valido")
