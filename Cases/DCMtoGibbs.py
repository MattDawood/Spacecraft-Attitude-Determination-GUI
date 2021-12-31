# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:05:32 2021

@author: Matthew
"""
import numpy as np

def Gibbs(values):
    ρ = [0] * 3
    matrix = np.zeros((3,3))
    # Converts values to floats then adds to new matrix
    for row in range(3):
        for col in range(3):
            for key, val in values.items():
                matrix[row][col] = float(values.get("a{}{}".format(row,col)).get())
                
    denom = 1 + matrix[0][0] + matrix[1][1] + matrix[2][2]
    
    ρ[0] = (1 / denom) * (matrix[1][2] - matrix[2][1])
    ρ[1] = (1 / denom) * (matrix[2][0] - matrix[0][2])
    ρ[2] = (1 / denom) * (matrix[0][1] - matrix[1][0])
    
    return ρ