# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 19:48:30 2021

@author: Matthew

Taken from matlab's dcm2quat function
"""
import numpy as np
from math import sqrt

def EulerParameters(values):
    matrix = np.zeros((3,3))
    EP = [0] * 4
    
    # Converts values to floats then adds to new matrix
    for row in range(3):
        for col in range(3):
            for key, val in values.items():
                matrix[row][col] = float(values.get("a{}{}".format(row,col)).get())
    
    matrix_tr = np.trace(matrix)
    
    if matrix_tr > 0:
        tr_sqrt   = sqrt(matrix_tr + 1)
        
        EP[0] = tr_sqrt * 0.5
        EP[1] = (matrix[1][2] - matrix[2][1]) / (2 * tr_sqrt)
        EP[2] = (matrix[2][0] - matrix[0][2]) / (2 * tr_sqrt)
        EP[3] = (matrix[0][1] - matrix[1][0]) / (2 * tr_sqrt)
        
    else:
        d = np.diagonal(matrix)
        
        # Max value at matrix[1][1]
        if ((d[1] > d[0]) and (d[1] > d[2])):
            sq_diag = sqrt(d[1] - d[2] - d[0] + 1)
            
            EP[2] = 0.5 * sq_diag
            
            if sq_diag != 0:
                sq_diag = 0.5 / sq_diag
            
            EP[0] = (matrix[2][0] - matrix[0][2]) * sq_diag
            EP[1] = (matrix[0][1] + matrix[1][0]) * sq_diag
            EP[3] = (matrix[1][2] + matrix[2][1]) * sq_diag
            
        # Max value at matrix[2][2]
        elif (d[2] > d[1]):
            sq_diag = sqrt(d[2] - d[1] - d[0] + 1)
            
            EP[3] = 0.5 * sq_diag
            
            if sq_diag != 0:
                sq_diag = 0.5 / sq_diag
                
            EP[0] = (matrix[0][1] - matrix[1][0]) * sq_diag
            EP[1] = (matrix[2][0] + matrix[0][2]) * sq_diag
            EP[2] = (matrix[1][2] + matrix[2][1]) * sq_diag
        
        # Max value at matrix[0][0]
        else:
            sq_diag = sqrt(d[0] - d[2] - d[1] + 1)
            
            EP[1] = 0.5 * sq_diag
            
            if sq_diag != 0:
                sq_diag = 0.5 / sq_diag
            
            EP[0] = (matrix[1][2] - matrix[2][1]) * sq_diag
            EP[2] = (matrix[0][1] + matrix[1][0]) * sq_diag
            EP[3] = (matrix[2][0] + matrix[0][2]) * sq_diag
    
    return EP