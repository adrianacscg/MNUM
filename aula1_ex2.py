# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:29:45 2019

@author: Adriana
"""
from math import exp
from decimal import Decimal


x1 = 1;
x2 = 1;

while x1 <= 20:
    x1 = x1 +1;
    y1 = exp(x1);
    
while x2 <= 20:
    x2 = x2 + 0.1;
    y2 = exp(x2);
    
print(y1)
print(y2)
print(y2-y1)

a = '%.2E' % Decimal(y1);
b = '%.2E' % Decimal(y2);
c = '%.2E' % Decimal(y1-y2);


print(a)
print(b)
print(c)
