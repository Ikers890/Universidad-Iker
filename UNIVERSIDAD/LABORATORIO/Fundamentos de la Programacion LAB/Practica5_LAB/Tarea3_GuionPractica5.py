# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 18:38:23 2020

@author: Iker Cuadros y Raúl Gómez

Tarea 3 - Guion Practica 5
"""

def PedirHora ():
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
    
    return (hora,minuto,segs)

def main():
    
    hora,minuto,segs = PedirHora()
    print(hora, ":",minuto, ":",segs)
    
    
if __name__ == "__main__":
    main()