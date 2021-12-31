# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 21:19:36 2021

@author: Matthew
"""
import numpy as np
from math import cos, sin, radians


def DCM(mRP, unit):
    DCM = np.zeros((3,3))
    
    # Converts values to floats
    mRP_0 = float(mRP[0].get())
    mRP_1 = float(mRP[1].get())
    mRP_2 = float(mRP[2].get())
    
    if unit == "Degrees":
        θ     = radians(float(mRP[3].get()))
    
    else:
        θ     = float(mRP[3].get())
    
    DCM[0][0] = (1 - cos(θ)) * mRP_0**2 + cos(θ)
    DCM[0][1] = (1 - cos(θ)) * mRP_0 * mRP_1 - mRP_2 * sin(θ)
    DCM[0][1] = (1 - cos(θ)) * mRP_0 * mRP_2 + mRP_1 * sin(θ)
    
    DCM[1][0] = (1 - cos(θ)) * mRP_1 * mRP_0 + mRP_2 * sin(θ)
    DCM[1][1] = (1 - cos(θ)) * mRP_1**2 + cos(θ)
    DCM[1][2] = (1 - cos(θ)) * mRP_1 * mRP_2 - mRP_0 * sin(θ)
    
    DCM[2][0] = (1 - cos(θ)) * mRP_2 * mRP_0 - mRP_1 * sin(θ)
    DCM[2][1] = (1 - cos(θ)) * mRP_2 * mRP_1 - mRP_0 * sin(θ)
    DCM[2][2] = (1 - cos(θ)) * mRP_2**2 + cos(θ)
    
    return DCM