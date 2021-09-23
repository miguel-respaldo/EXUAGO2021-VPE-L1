#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
PROGRAMA QUE DICE EL MES INGRESADO EN LETRA 
"""

print("\t||INGRESA EL MES EN NUMERO||")
#SOLICITA AL USUARIO LOS DATOS
mes = eval(input("Ingresa el numero del mes: ")) 

#COMPARA Y EVALUA EL DATO INGRESADO Y DEVUELVE EL RESULTADO        
if(mes == 1):
    print("Tu mes es Enero")

elif(mes == 2 ):
    print("Tu mes es Febrero")

elif(mes == 3 ):
    print("Tu mes es Marzo")

elif(mes == 4):
    print("Tu mes es Abril")

elif(mes == 5):
    print("Tu mes es Mayo")

elif(mes == 6):
    print("Tu me es Junio")

elif(mes == 7):
    print("Tu mes es Julio")

elif(mes == 8):
    print("Tu mes es Agosto")

elif(mes == 9):
    print("Tu mes es Septiembre")

elif(mes == 10):
    print("Tu mes es Octubre")

elif(mes == 11):
    print("Tu mes es Noviembre")

elif(mes == 12):
    print("Tu mes es Diciembre")

else:
    print("Tu numero es invalido")
