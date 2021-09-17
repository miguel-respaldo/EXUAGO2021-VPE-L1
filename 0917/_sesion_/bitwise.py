#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

x = 22

print("x      =       {:>6b}".format(x))
print("x & 4  = {:>3d} = {:>6b}".format(x & 4, x & 4))
print("x | 1  = {:>3d} = {:>6b}".format(x | 1, x | 1))
print("x ^ 4  = {:>3d} = {:>6b}".format(x ^ 4, x ^ 4))
print("~x     = {:>3d} = {:>6b}".format(~x , ~x))

# x  = 22 -> 0000 0001 0110   En C un int son 4 bytes = 2^32 = 32bits
# ~x =>      1111 1110 1001 

# Complemento a 2 
# y = 2  ->  0010
# ~y  ->     1101
# y = -2 ->  1101 -> 1110
# z = -3 ->          1101
#      11

print("x << 1 = {:>3d} = {:>6b}".format(x << 1, x << 1))
print("x >> 2 = {:>3d} = {:>6b}".format(x >> 2, x >> 2))

