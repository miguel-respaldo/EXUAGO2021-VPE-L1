#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

frase = "Hola,Mundo,loco"

lista = frase.split(",")
lista2= frase.split("o")

print(frase)
print(lista)
print(lista2)



print(len(lista))

f1,f2,f3 = lista
print(f1)
print(f2)
print(f3)

print("-----------")
print(lista[0])
print(lista[1])
print(lista[2])

print("-----------")
for f in lista:
    print(f)

print("************")


frase = "Hola ja Mundo ja Loco y cruel ja"

print(frase.split(" "))
print(frase.split("ja"))
