# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:20:48 2019

@author: Adriana
"""
from math import e
#Aula Prática 08/10/19 

def equacao(x):
    return e**(0.7*x)-x**2-0.5;

print("cálculo da bisseção pelo número de iteracões: ")

def bissection(a, b, numIt):        #cálculo da bisseção pelo número de iteracões
    m = 0;
    counter = 0;
    
    for i in range(0, numIt):
        
        print("");
        print("ITERAÇAO ", i);
        
        print("a: ","%.5f" % a);
        print("b: ","%.5f" % b);
        
        print("f(a): ","%.5f" % equacao(a));
        print("f(b: ","%.5f" % equacao(b));
        
        m = (a+b)/2;
       
        if(equacao(a) * equacao(m) >= 0):
            a = m;
        else:
            b = m;
            
        counter+= 1;
    
        print("m: ","%.5f" % m);
        
        print("f(m): ","%.5f" % equacao(m));
        
    print("residuo: ",equacao(m));
        
    print("")
    print("RAIZ: ")
    return (a+b)/2;

print(bissection(-1, 0, 4))

print("")
print("")
print("cálculo da bisseção pela precisão: ")

def bissec(a,b, p):             #cálculo da bisseção pela precisão
    while abs(a-b) > p:
        print("")
        print("a: ","%.5f" % a);
        print("b: ","%.5f" % b);
        
        print("f(a): ","%.5f" % equacao(a));
        print("f(b: ","%.5f" % equacao(b));
        
        m = (a+b)/2;
       
        if(equacao(a) * equacao(m) < 0):
            b = m;
        else:
            a = m;
            
        print("m: ","%.5f" % m);
        
        print("f(m): ","%.5f" % equacao(m));
        
        print("RAIZ: ", (a+b)/2)
        
    
    print("residuo: ",equacao(m));
    
    print("")
    print("RAIZ: ")
    
    return (a+b)/2;

print(bissec(-1.0,0.0,0.1))
   


    
    
    
    
    
    