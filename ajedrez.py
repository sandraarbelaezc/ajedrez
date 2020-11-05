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
        posiciones = []
        for i in movimientos:
            if i[0] >=0 and i[1] >=0:
                posiciones.append(i)
        for i in posiciones:
            self.tablero[i[0]][i[1]] = 1
        return self.tablero
    
    def pintar_mov_2(self, movimientos):
        posiciones = []
        for i in movimientos:
            for j in i:
                if j[0] >=0 and j[1] >=0:
                    posiciones.append(j)
        for i in posiciones:
            self.tablero[i[0]][i[1]] = 1
        return self.tablero
