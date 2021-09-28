#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

lista = ["manzana", "platano", "cereza", "limon", "kiwi", "mango", "melon",
        "mango", "manzana", "platano"]

print(lista)
lista.remove("cereza") # el elemnto a quitar
print(lista)
lista.pop(1) # el indice a quitar
print(lista)
lista.pop() # el último
print(lista)

if "mango" in lista:
    lista.remove("mango")
print(lista)


print("Quitamos manzana")
while "manzana" in lista:
    lista.remove("manzana")
print(lista)

