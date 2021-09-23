#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Se pide al usuario que ingrese un numero
mes = eval(input("Ingresa un numero y te regresare el mes correspondiente:"))

#Se evalua a que mes corresponde el numero ingresado
if mes == 12: print("El mes es Diciembre")
elif mes == 11: print("El mes es Noviembre")
elif mes == 10: print("El mes es Octubre")
elif mes == 9: print("El mes es Septiembre")
elif mes == 8: print("El mes es Agosto")
elif mes == 7: print("El mes es Julio")
elif mes == 6: print("El mes es Junio")
elif mes == 5: print("El mes es Mayo")
elif mes == 4: print("El mes es Abril")
elif mes == 3: print("El mes es Marzo")
elif mes == 2: print("El mes es Febrero")
elif mes == 1: print("El mes es Enero")
else: print("Mes inexistente")
