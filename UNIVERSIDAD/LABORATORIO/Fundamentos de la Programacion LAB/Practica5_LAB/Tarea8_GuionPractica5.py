# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:38:23 2020

@author: Iker Cuadros y Raúl Gómez

Tarea 8 - Guion Practica 5
"""

def contador (num):
    print (num)
    while num > 0:
        num -= 1
        print ("Contador descendente:\n",num)
        
    return(num)
        
def main():
    
    num = int(input("Dame numero inicial: "))
    
    print ("Contador descendente: ")
    contador(num)
   
if __name__ == "__main__":
    main()