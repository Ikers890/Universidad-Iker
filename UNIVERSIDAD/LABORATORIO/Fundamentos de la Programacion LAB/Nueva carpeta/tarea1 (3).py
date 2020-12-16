# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 17:39:36 2020
#Programa al que le pasemos una frase y muestre por pantalla cada una de las 
palabras que la forman 
#La frase solo contendrá palabras y separadores de palabras
@author: Ismael Gómez Argente
"""
import string

def ExtraerEntero(frase:str)->str:
    frase2 = ""
    for c in frase:
        if c in string.digits:
            frase2 += c
        elif not c in string.digits:
            frase += ""
        else:
            print("0")
            
    return frase2
'''
def LimpiarPalabra(frase1:str)->str:
    frase2 = ""
    for c in frase1:
        if not c in string.punctuation:
            frase2 += c
            
    return frase2
    
def SepararPalabras(frase1:str, palabra_recibida:str)->str:

    palabra = ""
    acum = ""
    linea = 1
    for c in frase1:
        if not c in string.whitespace:
            palabra += c
        else:
            if palabra == palabra_recibida:
                acum += str(linea) + " "
            palabra=""
            if c == '\n':
                linea += 1
    return acum

'''
def main():
    '''
     fichero = input("Dame el nombre del fichero: ")
     try: 
       fichero_in =  open(fichero, encoding = 'UTF-8')
     except:
        print("Ha ocurrido un error")
     else:
        pal_bus = input("Dime la palabra que quieres buscar: ")
        palabra = fichero_in.read()
        print(SepararPalabras(palabra, pal_bus))
    '''
    fichero = input("Dame el nombre del fichero: ")
    try:
        fichero = open(fichero, encoding='UTF-8')
    except:
        print("Se ha producido un error")
    else:
        num_bus = int(input("Dame el numero : "))
        num = fichero.read()
        resultado = int(ExtraerEntero(num))
        acum = 0
        if resultado % num_bus == 0:
            acum += num
        print(acum)
                
if __name__ == '__main__':
    main()
