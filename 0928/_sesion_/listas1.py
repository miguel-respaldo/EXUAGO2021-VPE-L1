#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

lista = ["manzana", "platano", "cereza", "limon", "kiwi", "mango", "melon"]

otra_lista = lista[2:5]

print(otra_lista)
print(lista[2:5])

print("-----------------")

print("Desde el inicio hasta menor a 5", lista[:5])
print("Desde el 2 hasta el final", lista[2:])

print("-----------------")

print(lista[-4:-1])
print("-----------------")

print("Tiene",len(lista),"elementos")
print(lista)
lista.insert(2,"naranja")
print(lista)
print("Tiene",len(lista),"elementos")
lista.insert(10,"sandia")
print(lista)
print("Tiene",len(lista),"elementos")
print(lista[-1])
print(lista[8])


