#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

valor = b'\x41\x42'

print("El valor es:", valor)

valor = b'\x00\x10'

entero_little = int.from_bytes(valor, "little")

print("En entero little es:", entero_little)

entero_big = int.from_bytes(valor, "big")

print("En entero big es:", entero_big)

