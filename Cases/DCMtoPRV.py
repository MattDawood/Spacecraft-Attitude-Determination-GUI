# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:11:14 2021

@author: Matthew
"""

import numpy as np
from math import atan2, degrees


def PrincipalRotationVector(values: list, unit: str) -> list:
    PRV = [0] * 4
    matrix = np.zeros((3,3))
    # Converts values to floats then adds to new matrix
    for row in range(3):
        for col in range(3):
            for key, val in values.items():
                matrix[row][col] = float(values.get("a{}{}".format(row,col)).get())
                
    X = matrix[2][1] - matrix[1][2]
    Y = matrix[0][2] - matrix[2][1]
    Z = matrix[1][0] - matrix[0][1]
    
    denom =(X**2 + Y**2 + Z**2)**0.5
    
    PRV[0] = X/denom
    PRV[1] = Y/denom
    PRV[2] = Z/denom
    
    if unit == 'Degrees':
        PRV[3] = degrees(atan2(denom, np.trace(matrix) - 1))
        
    else:
        PRV[3] = atan2(denom, np.trace(matrix) - 1)
    
    return PRV