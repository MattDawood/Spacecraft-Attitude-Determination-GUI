# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:30:32 2021

@author: Matthew
"""
import numpy as np
from math import sqrt

def EulerParameters(ρ):
    EP = [0] * 4
    ρ_new = [0] * 3
    # Converts values to floats
    for i in range(len(ρ)):
        ρ_new[i] = float(ρ[i].get())
    
    
    EP[0] = 1/ sqrt(1 + np.matmul(np.transpose(ρ_new), ρ_new))
    EP[1] = ρ_new[0] * EP[0]
    EP[2] = ρ_new[1] * EP[0]
    EP[3] = ρ_new[2] * EP[0]
    
    return EP