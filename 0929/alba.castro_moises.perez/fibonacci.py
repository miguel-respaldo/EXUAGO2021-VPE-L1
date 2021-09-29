#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# 0 1 1 2 3 5
# 0 1 2 3 4 5
def fibonacci(n):
    
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        f1 = 0
        f2 = 0
        f3 = 0
        for i in range(n):
            f1 = i
            f2 = i-1
            f3 = f1+f2
        
        return f3

def main():
    numero = int(input("Escribe un número para calcular su serie de fibonacci: "))
    
    print("La posición de la serie de fibonacci es ", fibonacci(numero)) 
    #format(numero,fibonacci(numero)))
        
if __name__ == "__main__":
    main()
