# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:38:23 2020

@author: Iker Cuadros y Raúl Gómez

Tarea 9 - Guion Practica 5
"""

def Fibonacci(num):
    if num==0 or num==1:
        numero = num
    else:
        numero = Fibonacci(num-1)+Fibonacci(num-2)
    return (numero)

def main ():
    num = int(input("Dame numero de fibonacci: "))
    print(Fibonacci(num))
    
if __name__ == "__main__":
    main()