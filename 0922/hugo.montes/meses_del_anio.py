#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

#Programa que dice el mes del año sgun el numero que incerte
print("meses del año")

#ingresa el numero del mes deseado
mes_num = int(input("ingrese el numero del mes que desea saber \n"))

#se busca el mes deseado entre las opciones

if mes_num == 1: print("ENERO")
elif mes_num == 2: print("FEBRERO")
elif mes_num == 3: print("MARZO")
elif mes_num == 4: print("ABRIL")
elif mes_num == 5: print("MAYO")
elif mes_num == 6: print("JUNIO")
elif mes_num == 7: print("JULIO")
elif mes_num == 8: print("AGOSTO")
elif mes_num == 9: print("SEPTIEMBRE")
elif mes_num == 10: print("OCTUBRE")
elif mes_num == 11: print("NOVIEMBRE")
elif mes_num == 12: print("DICIEMBRE")
else: print("Mes invalido")
