# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:20:48 2019

@author: Adriana
"""

#Aula Prática 08/10/19 

def equacao(x):
    return 2*x**2 - 5*x -2;

def bissection(a, b, numIt):        #cálculo da bisseção pelo número de iteracões
    m = 0;
    counter = 0;
    
    for i in range(0, numIt):
        
        m = (a+b)/2;
       
        if(equacao(a) * equacao(m) >= 0):
            a = m;
        else:
            b = m;
            
        counter+= 1;
    
    print("%.5f" % a);
    print("%.5f" % b);
    print("%.5f" % m);
    print("residuo: ",equacao(m));
        
    return (a+b)/2;

print(bissection(-1, 0, 25))

print("função 2: ")

def bissec(a,b, p):             #cálculo da bisseção pela precisão
    while abs(a-b) > p:
        
        m = (a+b)/2;
       
        if(equacao(a) * equacao(m) < 0):
            b = m;
        else:
            a = m;
        
    print("%.5f" % a);
    print("%.5f" % b);
    print("%.5f" % m);
    print("residuo: ",equacao(m));
    
    return (a+b)/2;

print(bissec(-0.35079,-0.35077,0.00001))
   
    
    
    
    
    
    
    
    