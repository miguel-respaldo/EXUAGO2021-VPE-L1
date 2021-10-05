#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Little Endian
#          33221100
numero = 0xAABBCCDD
#        0x000000FF
#        0x0000FF00
#        0x00FF0000
#          <----

print("{:x}".format(numero))
print("{:x}".format(numero & 0xFF))
print("{:x}".format(numero & 0xFF00))
print("{:x}".format(numero & 0xFF0000))

# Big Endian
#          00112233
numero = 0xAABBCCDD
#        0xFF     ->  AA000000
#        0xFF00   ->  AA
#          ---->
