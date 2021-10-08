#!/usr/bin/env python3

import os

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("El archivo demo.txt no existe") 
