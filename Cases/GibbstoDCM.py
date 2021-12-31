# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:36:39 2021

@author: Matthew
"""
import numpy as np

def DCM(ρ):
    DCM = np.zeros((3,3))
    
    # Converts values to floats
    ρ0 = float(ρ[0].get())
    ρ1 = float(ρ[1].get())
    ρ2 = float(ρ[2].get())
    
    
    denom = 1 + ρ0**2 + ρ1**2 + ρ2**2
    
    DCM[0][0] = 1 + ρ0**2 - ρ1**2 - ρ2**2
    DCM[0][1] = 2 * (ρ0 * ρ1 + ρ2)
    DCM[0][2] = 2 * (ρ0 * ρ2 - ρ1)
    
    DCM[1][0] = 2 * (ρ0 * ρ1 - ρ2)
    DCM[1][1] = 1 - ρ0**2 + ρ1**2 - ρ2**2
    DCM[1][2] = 2 * (ρ1 * ρ2 + ρ0)
    
    DCM[2][0] = 2 * (ρ0 * ρ2 + ρ1)
    DCM[2][1] = 2 * (ρ1 * ρ2 - ρ0)
    DCM[2][2] = 1 - ρ0**2 - ρ1**2 + ρ2**2
    
    
    DCM = (1 / denom) * DCM
    
    return DCM