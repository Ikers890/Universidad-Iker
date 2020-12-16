# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:38:23 2020

@author: Iker Cuadros y Raúl Gómez

Tarea 6 - Guion Practica 5
"""

def VerHoraNum (numero):
    hora = numero // 10000
    numero = numero % 10000
    minutos = numero // 100
    segs = numero % 100
    mod = print (hora,":", minutos,":", segs)
    return (mod)

def main():
    
    numero = int(input("Dame un numero positivo de 6 cifras obligatoriamente: "))
    while numero >= 1000000 or numero < 100000:
        numero = int(input("Dame un numero positivo de 6 cifras obligatoriamente: "))  
    
    VerHoraNum(numero)
    
    
if __name__ == "__main__":
    main()