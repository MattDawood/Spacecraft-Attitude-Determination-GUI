# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:01:56 2021

@author: Matthew
"""
import numpy as np
from math import cos, sin, radians


def value_convert(values, unit):
    """
    Converts values to floats, if units are in degrees converts to radians
    inorder to adhere to python's math functions'
    """
    a1 = float(values[0].get())
    a2 = float(values[1].get())
    a3 = float(values[2].get())
    
    if unit == "Degrees":
        
        a1 = radians(a1)
        a2 = radians(a2)
        a3 = radians(a3)
    
    return [a1, a2, a3]

def DCM121(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([1, 0, 0],
          [0, cos(a1), sin(a1)],
          [0, -sin(a1), cos(a1)])
    
    r2 = ([cos(a2), 0, -sin(a2)],
          [0, 1, 0],
          [sin(a2), 0, cos(a2)])
    
    r3 = ([1, 0, 0],
          [0, cos(a3), sin(a3)],
          [0, -sin(a3), cos(a3)])
    
    return martix_multiplicaton(r1,r2,r3)


def DCM123(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([1, 0, 0],
          [0, cos(a1), sin(a1)],
          [0, -sin(a1), cos(a1)])
    
    r2 = ([cos(a2), 0, -sin(a2)],
          [0, 1, 0],
          [sin(a2), 0, cos(a2)])
    
    r3 = ([cos(a3), sin(a3), 0],
          [-sin(a3), cos(a3), 0],
          [0, 0, 1])
    
    return martix_multiplicaton(r1,r2,r3)


def DCM131(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([1, 0, 0],
          [0, cos(a1), sin(a1)],
          [0, -sin(a1), cos(a1)])
    
    r2 = ([cos(a2), sin(a2), 0],
          [-sin(a2), cos(a2), 0],
          [0, 0, 1])
    
    r3 = ([1, 0, 0],
          [0, cos(a3), sin(a3)],
          [0, -sin(a3), cos(a3)])
    
    return martix_multiplicaton(r1,r2,r3)
    

def DCM132(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([1, 0, 0],
          [0, cos(a1), sin(a1)],
          [0, -sin(a1), cos(a1)])
    
    r2 = ([cos(a2), sin(a2), 0],
          [-sin(a2), cos(a2), 0],
          [0, 0, 1])
    
    r3 = ([cos(a3), 0, -sin(a3)],
          [0, 1, 0],
          [sin(a3), 0, cos(a3)])
    
    return martix_multiplicaton(r1,r2,r3)
    

def DCM212(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([cos(a1), 0, -sin(a1)],
          [0, 1, 0],
          [sin(a1), 0, cos(a1)])
    
    r2 = ([1, 0, 0],
          [0, cos(a2), sin(a2)],
          [0, -sin(a2), cos(a2)])
    
    r3 = ([cos(a3), 0, -sin(a3)],
          [0, 1, 0],
          [sin(a3), 0, cos(a3)])
    
    return martix_multiplicaton(r1,r2,r3)
 

def DCM213(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([cos(a1), 0, -sin(a1)],
          [0, 1, 0],
          [sin(a1), 0, cos(a1)])
    
    r2 = ([1, 0, 0],
          [0, cos(a2), sin(a2)],
          [0, -sin(a2), cos(a2)])
    
    r3 = ([cos(a3), sin(a3), 0],
          [-sin(a3), cos(a3), 0],
          [0, 0, 1])
    
    return martix_multiplicaton(r1,r2,r3)  


def DCM231(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([cos(a1), 0, -sin(a1)],
          [0, 1, 0],
          [sin(a1), 0, cos(a1)])
    
    r2 = ([cos(a2), sin(a2), 0],
          [-sin(a2), cos(a2), 0],
          [0, 0, 1])
    
    r3 = ([1, 0, 0],
          [0, cos(a3), sin(a3)],
          [0, -sin(a3), cos(a3)])
    
    return martix_multiplicaton(r1,r2,r3)  

    
def DCM232(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([cos(a1), 0, -sin(a1)],
          [0, 1, 0],
          [sin(a1), 0, cos(a1)])
    
    r2 = ([cos(a2), sin(a2), 0],
          [-sin(a2), cos(a2), 0],
          [0, 0, 1])
    
    r3 = ([cos(a3), 0, -sin(a3)],
          [0, 1, 0],
          [sin(a3), 0, cos(a3)])
    
    return martix_multiplicaton(r1,r2,r3)


def DCM312(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([cos(a1), sin(a1), 0],
          [-sin(a1), cos(a1), 0],
          [0, 0, 1])
    
    r2 = ([1, 0, 0],
          [0, cos(a2), sin(a2)],
          [0, -sin(a2), cos(a2)])
    
    r3 = ([cos(a3), 0, -sin(a3)],
          [0, 1, 0],
          [sin(a3), 0, cos(a3)])
    
    return martix_multiplicaton(r1,r2,r3)


def DCM313(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([cos(a1), sin(a1), 0],
          [-sin(a1), cos(a1), 0],
          [0, 0, 1])
    
    r2 = ([1, 0, 0],
          [0, cos(a2), sin(a2)],
          [0, -sin(a2), cos(a2)])
    
    r3 = ([cos(a3), sin(a3), 0],
          [-sin(a3), cos(a3), 0],
          [0, 0, 1])
    
    return martix_multiplicaton(r1,r2,r3)


def DCM321(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([cos(a1), sin(a1), 0],
          [-sin(a1), cos(a1), 0],
          [0, 0, 1])
    
    r2 = ([cos(a2), 0, -sin(a2)],
          [0, 1, 0],
          [sin(a2), 0, cos(a2)])
    
    r3 = ([1, 0, 0],
          [0, cos(a3), sin(a3)],
          [0, -sin(a3), cos(a3)])
    
    return martix_multiplicaton(r1,r2,r3)


def DCM323(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    r1 = ([cos(a1), sin(a1), 0],
          [-sin(a1), cos(a1), 0],
          [0, 0, 1])
    
    r2 = ([cos(a2), 0, -sin(a2)],
          [0, 1, 0],
          [sin(a2), 0, cos(a2)])
    
    r3 = ([cos(a3), sin(a3), 0],
          [-sin(a3), cos(a3), 0],
          [0, 0, 1])
    
    return martix_multiplicaton(r1,r2,r3) 
    
 
def martix_multiplicaton(R1, R2, R3):
    result = np.matmul(np.matmul(R3,R2),R1)
    
    return result
