#!/usr/bin/python
# -*- coding: utf-8 -*- 
import re

def suma(a,b):
    return a+b
    
if __name__ == "__main__":
    num = 0

    while True:
        entrada = raw_input('= '+str(num)+' ')
        m = re.search('([+-/*//]\s?)([0-9]*)', entrada)
        op = m.group(1).strip()
        b = int(m.group(2))
        
        if op == '+':
            num = suma(num,b)
            
        