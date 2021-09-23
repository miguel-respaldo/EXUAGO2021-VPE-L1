#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later


#Solicitar numero al usuario en el rango (1-12)
mes = int(input("Ingresa un numero de 1-12: "))

#Codigo que calcula el modulo de cualquier numero
if mes == 1: print("El numero",mes,"corresponde a Enero")
elif mes == 2: print("El numero",mes,"corresponde a Febrero")
elif mes == 3: print("El numero",mes,"corresponde a Marzo")
elif mes == 4: print("El numero",mes,"corresponde a Abril")
elif mes == 5: print("El numero",mes,"corresponde a Mayo")
elif mes == 6: print("El numero",mes,"corresponde a Junio")
elif mes == 7: print("El numero",mes,"corresponde a Julio")
elif mes == 8: print("El numero",mes,"corresponde a Agosto")
elif mes == 9: print("El numero",mes,"corresponde a Septiembre")
elif mes == 10: print("El numero",mes,"corresponde a Octubre")
elif mes == 11: print("El numero",mes,"corresponde a Noviembre")
elif mes == 12: print("El numero",mes,"corresponde a Diciembre")
else:
    print("Numero invalido")

