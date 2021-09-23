#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Programa que me diga el mes del anio y me diga el mes
en letras.
"""

#Lista que contiene los meses en texto.
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
        "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

#Despliegue de mensaje descriptivo al usuario.
print("""Programa que determina a que mes pertenece un numero
ingresado.""")

#Solicitud e ingreso de los datos.
mes = eval (input("Ingrese el numero del mes: "))

#Despliegue del resultado.
print("El mes correspondiente a", mes, "es", meses[mes-1])
