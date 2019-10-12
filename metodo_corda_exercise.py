# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:42:29 2019

@author: Adriana
"""

def equacao(x):
    return 2*x**2 - 5*x -2;

def bissection(a, b, numIt):
    r = (a * equacao(b) - b * equacao(a)) / (equacao(b) - equacao(a));
    
    for i in range(0, numIt):
       
        if(equacao(a) * equacao(r) < 0):
            b = r;
            print("b: ",b);
        else:
            a = r;
            print("a: ",a);
            
        r = (a * equacao(b) - b * equacao(a)) / (equacao(b) - equacao(a));
        
        
    print("%.5f" % a);
    print("%.5f" % b);
    print("%.5f" % r);
        
    return r;

print(bissection(0, 1,17))