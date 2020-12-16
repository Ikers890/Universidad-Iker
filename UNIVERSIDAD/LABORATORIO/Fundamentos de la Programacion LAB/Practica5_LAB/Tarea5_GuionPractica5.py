# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:38:23 2020

@author: Iker Cuadros y Raúl Gómez

Tarea 5 - Guion Practica 5
"""
def ConvertirHoraNum (hora, minuto, segs):
    res = (hora * 10000) + (minuto * 100) + segs
    return (res)
    # Esta función será útil en nuestro programa para guardar una hora (3 números) en una sola
    # variable.
    # Además, si un número calculado de esta forma es mayor que otro, sus horas
    # correspondientes guardarán esa misma relación, por lo que será útil más adelante para
    # comparar horas. 

def main():
    hora = int(input("Dime la hora: "))
    while hora>24 or hora <0:
        print("Hora erronea")
        hora = int(input("Dime la hora: "))
        
    minuto = int(input("Dime los minutos: "))
    while minuto>60 or minuto <0:
        print("Minutos erroneoa")
        minuto = int(input("Dime los minutos: "))
        
    segs = int(input("Dime los segundos: "))
    while segs>60 or segs <0:
        print("Segundos erroneos")
        segs = int(input("Dime los segundos: "))
    
    res =   ConvertirHoraNum(hora, minuto, segs)
    print(res)
if __name__ =="__main__":
    main()