# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:46:12 2021

@author: Matthew
"""
import numpy as np
from math import sin, cos,radians

def DCM(PRV, unit):
    DCM = np.zeros((3,3))
    
    # Converts values to floats
    PRV_0 = float(PRV[0].get())
    PRV_1 = float(PRV[1].get())
    PRV_2 = float(PRV[2].get())
    
    if unit == "Degrees":
        theta = radians(float(PRV[3].get()))
        
    else:
        theta = float(PRV[3].get())
    
    DCM[0][0] = cos(theta) + (PRV_0 **2) * (1-cos(theta))
    DCM[0][1] = (PRV_0 * PRV_1 * (1-cos(theta))) - PRV_2 * sin(theta)
    DCM[0][2] = (PRV_0 * PRV_2 * (1-cos(theta))) + PRV_1 * sin(theta)
    
    DCM[1][0] = (PRV_1 * PRV_0 * (1-cos(theta))) + PRV_2 * sin(theta)
    DCM[1][1] = cos(theta) + (PRV_1 **2) * (1-cos(theta))
    DCM[1][2] = (PRV_2 * PRV_1 * (1-cos(theta))) - PRV_0 * sin(theta)
    
    DCM[2][0] = (PRV_2 * PRV_0 * (1-cos(theta))) - PRV_1 * sin(theta)
    DCM[2][1] = (PRV_2 * PRV_1 * (1-cos(theta))) + PRV_0 * sin(theta)
    DCM[2][2] = cos(theta) + (PRV_2 **2) * (1-cos(theta))
    
    return DCM