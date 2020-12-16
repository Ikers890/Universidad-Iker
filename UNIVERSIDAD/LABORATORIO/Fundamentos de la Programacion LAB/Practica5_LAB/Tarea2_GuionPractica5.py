# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:15:14 2020

@author: Iker Cuadros y Raúl Gómez

Tarea 2 - Guion Practica 5
"""
def PedirNumero (lim_sup: float, lim_inf:float):
    
    num = float(input("[Entre el  limite inferior y el limite superior, ambos incluidos]: "))
    return num

def main():
    
    lim_sup = float(input("Dame un numero para usarlo como limite superior: "))
    lim_inf = float(input("Dame un numero para usarlo como limite inferior: "))
    
    num = PedirNumero(lim_sup, lim_inf)
    if num <= lim_sup and num >= lim_inf:
        print("El numero ", num, " está en el rango") 
    else:
        while num > lim_sup or num < lim_inf:
            print("----> ERROR: Fuera del rango [" , lim_inf,",",lim_sup,"]")
            num = PedirNumero(lim_sup, lim_inf)
        print("El numero ", num, " está en el rango") 
        
    
if __name__ == "__main__":
    main()