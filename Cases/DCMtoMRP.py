# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:20:12 2021

@author: Matthew
"""
import numpy as np
from math import sin, acos, degrees, radians

def ModifiedRodriguesParameters(values: list, unit: str):
    MRP = [0] * 4
    matrix = np.zeros((3,3))
    # Converts values to floats then adds to new matrix
    for row in range(3):
        for col in range(3):
            for key, val in values.items():
                matrix[row][col] = float(values.get("a{}{}".format(row,col)).get())
    
    if unit == 'Degrees':
        MRP[3]      = degrees(acos((np.trace(matrix) - 1) / 2))
        MRP[0] = -(matrix[2][1] - matrix[1][2]) /  2 * sin(radians(MRP[3]))
        MRP[1] = -(matrix[0][2] - matrix[2][0]) /  2 * sin(radians(MRP[3]))
        MRP[2] = -(matrix[1][0] - matrix[0][1]) /  2 * sin(radians(MRP[3]))
    
    else:
        MRP[3]      = acos((np.trace(matrix) - 1) / 2)
        MRP[0] = -(matrix[2][1] - matrix[1][2]) /  2 * sin((MRP[3]))
        MRP[1] = -(matrix[0][2] - matrix[2][0]) /  2 * sin((MRP[3]))
        MRP[2] = -(matrix[1][0] - matrix[0][1]) /  2 * sin((MRP[3]))
    
    return MRP

