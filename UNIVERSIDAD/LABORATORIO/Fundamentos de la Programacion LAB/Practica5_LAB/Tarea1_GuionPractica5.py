# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:44:10 2020

@author: Iker Cuadros y Raúl Gómez

Tarea 1 - Guion Practica 5
"""
def NumeroEnRango(num: bool, lim_inf: float, lim_sup: float):
    if num >= lim_inf and num<=lim_sup:
        numB = True
    else: 
        numB = False
        
    return numB

def main():

    print(__doc__)
    num = float(input("Dame un numero cualquiera: "))
    lim_sup = float(input("Dame un numero para usarlo como limite superior: "))
    lim_inf = float(input("Dame un numero para usarlo como limite inferior: "))
    while lim_inf > lim_sup:
        lim_inf = float(input("Dame un numero para usarlo como limite inferior: "))
    
    numB = NumeroEnRango(num, lim_inf, lim_sup) 
    if numB==True:
        print("El numero esta entre los limites")
    else:
        print("El numero no esta entre los limites")
    
if __name__ == "__main__":
    main()

