# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 00:32:27 2021

@author: Matthew
"""
from math import cos, sin, radians

e  = [0] * 5

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


def EP121(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] = cos(0.5*(a1+a3))*cos(0.5*a2)
    e[1] = sin(0.5*(a1+a3))*cos(0.5*a2)
    e[2] = cos(0.5*(a1-a3))*sin(0.5*a2)
    e[3] = sin(0.5*(a1-a3))*sin(0.5*a2)
    
    return e

    
def EP123(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] = -sin(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)+cos(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)
    e[1] =  sin(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)+cos(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)
    e[2] = -sin(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)+cos(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)
    e[3] =  sin(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)+cos(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)
    
    return e
    

def EP131(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] =  cos(0.5*(a1+a3))*cos(0.5*a2)
    e[1] =  sin(0.5*(a1+a3))*cos(0.5*a2)
    e[2] = -sin(0.5*(a1-a3))*sin(0.5*a2)
    e[3] =  cos(0.5*(a1-a3))*sin(0.5*a2)   
    
    return e
    

def EP132(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] =  sin(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)+cos(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)
    e[1] =  sin(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)-cos(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)
    e[2] =  cos(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)-sin(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)
    e[3] =  cos(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)+sin(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)
    
    return e

    
def EP212(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] =  cos(0.5*(a1+a3))*cos(0.5*a2)
    e[1] =  cos(0.5*(a1-a3))*sin(0.5*a2)
    e[2] =  sin(0.5*(a1+a3))*cos(0.5*a2)
    e[3] = -sin(0.5*(a1-a3))*sin(0.5*a2)
        
    return e
    
def EP213(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] =  sin(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)+ cos(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)
    e[1] =  sin(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)+ cos(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)
    e[2] =  sin(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)- cos(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)
    e[3] = -sin(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)+ cos(a1*0.5)*cos(a2*0.5)*sin(a3*0.5) 
    
    return e
    
    
def EP231(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] = -sin(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)+ cos(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)
    e[1] =  sin(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)+ cos(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)
    e[2] =  sin(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)+ cos(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)
    e[3] = -sin(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)+ cos(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)   
        
    return e
    
    
def EP232(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] =  cos(0.5*(a1+a3))*cos(0.5*a2)
    e[1] =  sin(0.5*(a1-a3))*sin(0.5*a2)
    e[2] =  sin(0.5*(a1+a3))*cos(0.5*a2)
    e[3] =  cos(0.5*(a1-a3))*sin(0.5*a2)

    return e
    
    
def EP312(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] = -sin(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)+ cos(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)
    e[1] = -sin(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)+ cos(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)
    e[2] =  sin(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)+ cos(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)
    e[3] =  sin(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)+ cos(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)

    return e
    
    
def EP313(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] = cos(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)-sin(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)
    e[1] = cos(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)+sin(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)
    e[2] = sin(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)-cos(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)
    e[3] = cos(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)+sin(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)
    
    return e
    
    
def EP321(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] =  sin(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)+ cos(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)
    e[1] = -sin(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)+ cos(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)
    e[2] =  sin(a1*0.5)*cos(a2*0.5)*sin(a3*0.5)+ cos(a1*0.5)*sin(a2*0.5)*cos(a3*0.5)
    e[3] =  sin(a1*0.5)*cos(a2*0.5)*cos(a3*0.5)- cos(a1*0.5)*sin(a2*0.5)*sin(a3*0.5)
    
    return e
    
    
def EP323(values, unit):
    a1, a2, a3 = value_convert(values, unit)
    
    e[0] =  cos(0.5*(a1+a3))*cos(0.5*a2)
    e[1] = -sin(0.5*(a1-a3))*sin(0.5*a2)
    e[2] =  cos(0.5*(a1-a3))*sin(0.5*a2)
    e[3] =  sin(0.5*(a1+a3))*cos(0.5*a2)
    
    return e