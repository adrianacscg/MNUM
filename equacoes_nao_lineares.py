# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:44:09 2019

@author: Adriana
"""
from math import log

def J(x,y):
    return -(2*y)/(x-1)-2*(x-3);

def hn(x,y):
    return -y**2+2*y*(y-log(x-1))-(x-3)**2+4;

def kn(x,y):
    return -((y**2+(x-3)**2-4)/(x-1))-2*(x-3)*(y-log(x-1));

def newton_eq_n_lineares(x,y, numIt):
    
    
    for i in range(numIt):
        x0 = x - (hn(x,y)/J(x,y));
        y0 = y - (kn(x,y)/J(x,y));
        
        x = x0;
        y = y0;
        
        print("x: ",x);
        print("y: ",y);
        
    return 0;


newton_eq_n_lineares(1.5,1.3,2)