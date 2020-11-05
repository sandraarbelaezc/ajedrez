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
