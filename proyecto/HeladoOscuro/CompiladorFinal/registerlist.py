#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
# dictionary used return the values of registers rs, rt, rd
# in diferent cases clasificated in mnemonics with opcode & func_type
registers = {
    "x0" : 0,
    "x1" : 1,
    "x2" : 2,
    "x3" : 3,
    "x4" : 4,
    "x5" : 5,
    "x6" : 6,
    "x7" : 7
}
labels = {
    "MAIN" : 1,
    "INC" : 4,
    "DEC" : 9,
    "FUNC" : 8,
    "EXIT" : 15
}

def reg_decode(func_type, instr, regs):
    
    #For the cases when func_type is equal "r"
    if func_type == "r":   
        
        #special case "sll" | "srl"
        if (instr == "sll") or (instr == "srl"): 
            try:
                if (regs[0] < regs[1]):
                    #return[rs,        rt,               rd,             filler]
                    return [registers[regs[1]], registers[regs[1]], registers[regs[1]], 0] 
                else:
                    #return[rs,        rt,               rd,             filler]
                    return [registers[regs[0]], registers[regs[1]], registers[regs[0]], 0] 
            except:
                return None                

        #special case for jr
        if (instr == "jr"): 
            try:
                #return[        rs,        rt, rd,filler]
                return [registers[regs[0]], 0, 0, 0]
            except:
                return None   
            
        #for the others when func_type is equal "r"           
        try:   
            #return[      rs,                 rt,               rd,          filler]    
            return[registers[regs[1]], registers[regs[2]], registers[regs[0]], 0]
        except:
            return None
            
    elif func_type == "b":
        try:
            return [registers[regs[0]], registers[regs[1]], labels[regs[2]]]    
        except:
            return None

    #For the cases when func_type is equal "i"
    elif func_type == "i":
            
        #special case for sb
        if (instr == "sb") or (instr == "lb"):
            try:
                if len(regs[1]) > 1 and regs[1][1] == "x":
                    imm = int(regs[1], base=16)
                else:
                    imm = int(regs[1])
            
                #return[       rs,                rt        ,  immediate  ]      
                return[registers[regs[2]], registers[regs[0]], imm]
            except:
                return None
                          
        
        #for the others when func_type is equal "i"       
        try:
            if len(regs[2]) > 1 and regs[2][1] == "x":
                imm = int(regs[2], base=16)
            else:
                imm = int(regs[2])
        
            #return[        rs                 rt             immediate ]
            return [registers[regs[1]], registers[regs[0]], imm]
        except:
            return None       
        
    
    #For the cases when func_type is equal "i" just in the case for hex
    elif func_type == "j":
        return [labels[regs[0]]]
      
    else:
        return None
