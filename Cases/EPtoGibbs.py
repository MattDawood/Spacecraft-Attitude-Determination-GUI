# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:28:16 2021

@author: Matthew
"""
def GibbsVector(Eulerparameters):
    ρ  = [0] * 3
    EP = [0] * 4

    # Converts values to floats
    EP[0] = float(EP[0].get())
    EP[1] = float(EP[1].get())
    EP[2] = float(EP[2].get())
    EP[3] = float(EP[3].get())
    
    ρ[0] = EP[1] / EP[0]
    ρ[1] = EP[2] / EP[0]
    ρ[2] = EP[3] / EP[0]
    
    return ρ