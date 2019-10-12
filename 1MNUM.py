# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 18:19:35 2019

@author: Adriana
"""
#quantia inicial = e-1
# 2ºano : (e-1)*1-1 = a
#3ªano : (e-1)*2-1 => a*2-1

#Quanto dinheiro temos na conta ao fim de 25 anos?
from math import e
from decimal import Decimal

def money():
   # inicial = e -1;
    ee = 2.718;
    print(e);
    
    total = ee -1;
    print(total)
    for i in range (1,26):
        total = total *i -1;
       
        
   
    
    x = '%.2E' % Decimal(total)
    return x;

print(money());


        
        

