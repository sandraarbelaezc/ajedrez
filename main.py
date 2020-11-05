#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ajedrez import ajedrez

def menu():
    pieza = input("Ingresa el nombre de la pieza de ajedrez: ")
    x,y = tuple(map(int,input("\nIngresa la posición de la pieza en el tablero: ").strip().split(',')))[:2]

    try:
        if pieza in ['rey', 'reina', 'torre', 'alfil', 'caballo', 'peon', 's'] and x <= 7 and x >= 0 and y <= 7 and y >= 0:
            return (pieza,x,y)
        else:
            print("Escoja una estas opciones: rey, reina, torre, alfil, caballo, peon. La posición debe ser entre 0 y 7, ejem: (0,7).")
            pieza = input("Ingresa el nombre de la pieza de ajedrez: ")
            x,y = tuple(map(int,input("\nIngresa la posición de la pieza en el tablero: ").strip().split(',')))[:2]
            return (pieza,x,y)
    except:
        print("Fin")

while(True):

    pieza, x, y = menu()
    juego = ajedrez(pieza, y, x)

    if pieza == "s":
        print("Fin")
        break
    elif pieza == "rey":
        juego.mov_rey(y,x)
    elif pieza == "reina":
        juego.mov_reina(y,x)
    elif pieza == "alfil":
        juego.mov_alfil(y,x)
    elif pieza == "torre":
        juego.mov_torre(y,x)
    elif pieza == "caballo":
        juego.mov_caballo(y,x)
    elif pieza == "peon":
        juego.mov_peon(y,x)