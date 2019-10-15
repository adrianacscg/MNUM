# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:40:14 2019

@author: Adriana
"""

#aula 15/10/19
#metodo de Newton e Picard Peano

from math import sqrt


def function(x, opcao):
    if opcao == 0:
        return 2*x**2 -5*x -3;          #expressao original
    elif opcao == 1:
        return 0.4*x**2-0.6;
    elif opcao == 2:
        return sqrt(2.5*x+15);
    elif opcao == 3:
        return -sqrt(2.5*x+15);
    elif opcao == 4:
        return 2.5 + 1.5*x;




def derivada(x):
    return 4*x-5;

def PicardPeano(guess, numIt):
    print("PICARD PEANO: ");
    exato = 1.25;
    
    while (abs(derivada(guess) <= 1)):
            
        guess = function(guess,0);
        print(guess, abs(guess-exato));
        
PicardPeano(0, 20)


def Newton(guess, numIt):
    print("NEWTON: ")
    for i in range (numIt):
        guess = guess - function(guess,0)/derivada(guess);
        print(guess);

Newton(2, 10)