# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 22:45:00 2021

@author: Matthew
"""
import numpy as np
from math import sqrt

def normalize(EP_matrix):
    sqrd_sum = sqrt(sum(x*x for x in EP_matrix))
    
    for i in range(len(EP_matrix)):
        EP_matrix[i] = EP_matrix[i] / sqrd_sum
        
    return EP_matrix

def DCM(EulerParameters):
    e    = [0] * 4
        
    # Converts values to floats
    e[0] = float(EulerParameters[0].get())
    e[1] = float(EulerParameters[1].get())
    e[2] = float(EulerParameters[2].get())
    e[3] = float(EulerParameters[3].get())
     
    e = normalize(e)
    
    DCM = np.zeros((3,3))
    
    DCM[0][0] = e[0]**2 + e[1]**2 - e[2]**2 - e[3]**2
    DCM[0][1] = 2 * (e[1] * e[2] + e[0] * e[3])
    DCM[0][2] = 2 * (e[1] * e[3] - e[0] * e[2])
    
    DCM[1][0] = 2 * (e[1] * e[2] - e[0] * e[3])
    DCM[1][1] = e[0]**2 - e[1]**2 + e[2]**2 - e[3]**2
    DCM[1][2] = 2 * (e[2] * e[3] + e[0] * e[1])
    
    DCM[2][0] = 2 * (e[1] * e[3] + e[0] * e[2])
    DCM[2][1] = 2 * (e[2] * e[3] - e[0] * e[1])
    DCM[2][2] = e[0]**2 - e[1]**2 - e[2]**2 + e[3]**2

    return DCM