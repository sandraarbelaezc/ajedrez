#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class ajedrez():

    def __init__(self, pieza, x, y):
        self.tablero = np.zeros((8,8))
        self.pieza = pieza
        self.x = x
        self.y = y
        self.tablero[x][y] = 8
    
    def pintar_mov_1(self, movimientos):
        '''argumentos de entrada: una lista con los posibles movimientos de la pieza
        retorna: el tablero con los movimientos marcados en 1, la posición de la ficha
        en 8 y el resto en 0'''

        posiciones = []
        for i in movimientos:
            if i[0] >=0 and i[1] >=0:
                posiciones.append(i)
        for i in posiciones:
            self.tablero[i[0]][i[1]] = 1
        return self.tablero
    
    def pintar_mov_2(self, movimientos):
        '''argumentos de entrada: una lista con los posibles movimientos de la pieza
        retorna: el tablero con los movimientos marcados en 1, la posición de la ficha
        en 8 y el resto en 0'''

        posiciones = []
        for i in movimientos:
            for j in i:
                if j[0] >=0 and j[1] >=0:
                    posiciones.append(j)
        for i in posiciones:
            self.tablero[i[0]][i[1]] = 1
        return self.tablero
    
    def mov_rey(self,x,y):
        '''argumentos de entrada: x,y posición del rey en el tablero
        retorna: los movimientos que puede hacer el rey'''

        movimientos = [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x-1,y-1),(x-1,y+1),(x+1,y+1),(x+1,y-1)]
        self.tablero = self.pintar_mov_1(movimientos)
        print("Rey")
        print(self.tablero)
    
    def mov_torre(self,x,y):
        '''argumentos de entrada: x,y posición de la torre en el tablero
        retorna: los movimientos que puede hacer la torre'''

        movimientos = [[(x+i,y) for i in range(1,7) if x+i <= 7],
                        [(x,y+i) for i in range(1,7) if y+i <= 7],
                        [(x-i,y) for i in range(1,7) if x-i >= 0],
                        [(x,y-i) for i in range(1,7) if y-i >= 0]]
        self.tablero = self.pintar_mov_2(movimientos)
        print("Torre")
        print(self.tablero)
    
    def mov_alfil(self,x,y):
        '''argumentos de entrada: x,y posición del alfil en el tablero
        retorna: los movimientos que puede hacer el alfil'''

        movimientos = [[(x-i,y-i) for i in range(1,7) if x-i >= 0 and y-i >= 0],
                        [(x-i,y+i) for i in range(1,7) if x-i >= 0 and y+i <= 7],
                        [(x+i,y-i) for i in range(1,7) if x+i <= 7 and y-i >=0],
                        [(x+i,y+i) for i in range(1,7) if x+i <= 7 and y+i <= 7]]
        self.tablero = self.pintar_mov_2(movimientos)
        print("Alfil")
        print(self.tablero)
    
    def mov_reina(self,x,y):
        '''argumentos de entrada: x,y posición de la reina en el tablero
        retorna: los movimientos que puede hacer la reina'''
        
        movimientos = [[(x+i,y) for i in range(1,7) if x+i <= 7],
                        [(x,y+i) for i in range(1,7) if y+i <= 7],
                        [(x-i,y) for i in range(1,7) if x-i >= 0],
                        [(x,y-i) for i in range(1,7) if y-i >= 0],
                        [(x-i,y-i) for i in range(1,7) if x-i >= 0 and y-i >= 0],
                        [(x-i,y+i) for i in range(1,7) if x-i >= 0 and y+i <= 7],
                        [(x+i,y-i) for i in range(1,7) if x+i <= 7 and y-i >=0],
                        [(x+i,y+i) for i in range(1,7) if x+i <= 7 and y+i <= 7]]
        self.tablero = self.pintar_mov_2(movimientos)
        print("Reina")
        print(self.tablero)
    
    def mov_caballo(self,x,y):
        '''argumentos de entrada: x,y posición del caballo en el tablero
        retorna: los movimientos que puede hacer el caballo'''

        movimientos = [(x+1,y-2),(x+2,y-1),(x+2,y+1),(x+1,y+2),(x-1,y+2),(x-2,y+1),(x-2,y-1),(x-1,y-2)]
        self.tablero = self.pintar_mov_1(movimientos)
        print("Caballo")
        print(self.tablero)
