#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:
#
# SPDX-License-Identifier: GPL-3.0-or-later


mis_bytes = bytearray(3)

print(mis_bytes)

mis_bytes[0] = 1 #  0000 0001
mis_bytes[1] = 2 #  0000 0010
mis_bytes[2] = 3 #  0000 0011

#         g         8         0
# 0000 0011 0000 0010 0000 0001

print("-----------")
print(mis_bytes)

