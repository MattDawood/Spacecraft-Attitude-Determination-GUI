# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:16:34 2021

@author: Matthew
"""
from math import acos, asin, atan2, degrees, sqrt

EA = [0] * 3

# Cant handle results > 1 or < -1Might need to Restructure

def normalize(EP_matrix):
    sqrd_sum = sqrt(sum(x*x for x in EP_matrix))
    
    for i in range(len(EP_matrix)):
        EP_matrix[i] = EP_matrix[i] / sqrd_sum
        
    return EP_matrix
        

def value_convert(values):
    EP_matrix = []
    
    # Converts values to floats
    EP_matrix.append(float(values[0].get()))
    EP_matrix.append(float(values[1].get()))
    EP_matrix.append(float(values[2].get()))
    EP_matrix.append(float(values[3].get()))

    EP_matrix = normalize(EP_matrix)

    return EP_matrix

def to_degrees(EulerAngles):
    for i in range(len(EulerAngles)):
        EulerAngles[i] = degrees(EulerAngles[i])
        
    return EulerAngles

def EA121(values):
    q = value_convert(values)
    
    EA[0] = atan2(2*(q[1]*q[2] + q[3]*q[0]), 2*(q[2]*q[0] - q[1]*q[3]))
    EA[1] = acos((q[0]**2) + (q[1]**2) - (q[2]**2) - (q[3]**2))
    EA[2] = atan2(2*(q[1]*q[2] - q[3]*q[0]), 2*(q[1]*q[3] + q[2]*q[0]))
    
    return EA


def EA123(values):
    q = value_convert(values)
    
    EA[0] = atan2(2 * (q[1]*q[0] - q[3]*q[2]),\
                  (q[0]**2) - (q[1]**2) - (q[2]**2) + (q[3]**2))
    
    if (2 * (q[1]*q[3] + q[2]*q[0])) > 1:
        EA[1] = asin(1)
        
    elif (2 * (q[1]*q[3] + q[2]*q[0])) < -1:
         EA[1] = asin(-1)
    
    else:
        EA[1] = asin(2 * (q[1]*q[3] + q[2]*q[0]))
    
    EA[2] = atan2(2 * (q[3]*q[0] - q[1]*q[2]),\
                  (q[0]**2) + (q[1]**2) - (q[2]**2) - (q[3]**2))
    
    return EA


def EA131(values):
    q = value_convert(values)
    
    EA[0] = atan2(2*(q[1]*q[3] - q[2]*q[0]), 2*(q[1]*q[2] + q[3]*q[0]))
    EA[1] = acos((q[0]**2) + (q[1]**2) - (q[2]**2) - (q[3]**2))
    EA[2] = atan2(2*(q[1]*q[3] + q[2]*q[0]), 2*(q[0]*q[3] - q[2]*q[1]))
    
    return EA


def EA132(values):
    q = value_convert(values)
    
    EA[0] = atan2(2 * (q[1]*q[0] + q[2]*q[3]),\
                  ((q[0]**2) - (q[1]**2) + (q[2]**2) - (q[3]**2)))
        
    EA[1] = asin(2 * (q[0]*q[3] - q[2]*q[1]))
    
    EA[2] = atan2(2 * (q[1]*q[3] + q[2]*q[0]),\
                  ((q[0]**2) + (q[1]**2) - (q[2]**2) - (q[3]**2)))
    
    return EA


def EA212(values):
    q = value_convert(values)
    
    EA[0] = atan2((q[1]*q[2] - q[3]*q[0]), (q[2]*q[3] + q[0]*q[1]))
    EA[1] = acos((q[0]**2) - (q[1]**2) + (q[2]**2) - (q[3]**2))
    EA[2] = atan2((q[1]*q[2] + q[3]*q[0]), (q[0]*q[1] - q[2]*q[3]))
    
    return EA


def EA213(values):
    q = value_convert(values)
    
    EA[0] = atan2(2 * (q[1]*q[3] + q[2]*q[0]),\
                  ((q[0]**2) - (q[1]**2) - (q[2]**2) + (q[3]**2)))
        
    EA[1] = asin(-2 * (q[2] * q[3] - q[0] * q[1]))
    
    EA[2] = atan2(2 * (q[1]*q[2] + q[3]*q[0]),\
                  ((q[0]**2) - (q[1]**2) + (q[2]**2) - (q[3]**2)))
    
    return EA


def EA231(values):
    q = value_convert(values)
    
    EA[0] = atan2(2 * (q[2]*q[0] - q[1]*q[3]),\
                  ((q[0]**2) + (q[1]**2) - (q[2]**2) - (q[3]**2)))
        
    EA[1] = asin(2 * (q[2]*q[1] + q[0]*q[3]))
    
    EA[2] = atan2(2 * (q[1]*q[0] - q[3]*q[2]),\
                  ((q[0]**2) - (q[1]**2) + (q[2]**2) - (q[3]**2)))
    
    return EA


def EA232(values):
    q = value_convert(values)
    
    EA[0] = atan2((q[0]*q[1] + q[2]*q[3]), (q[0]*q[3] - q[1]*q[2]))
    
    if ((q[0]**2) - (q[1]**2) + (q[2]**2) - (q[3]**2)) > 1:
        EA[1] = acos(1)
    
    elif ((q[0]**2) - (q[1]**2) + (q[2]**2) - (q[3]**2)) < -1:
        EA[1] = acos(-1)
    
    else:
        EA[1] = acos((q[0]**2) - (q[1]**2) + (q[2]**2) - (q[3]**2))
        
    EA[2] = atan2((q[2]*q[3] - q[0]*q[1]), (q[1]*q[2] + q[0]*q[3]))
    
    return EA


def EA312(values):
    q = value_convert(values)
    
    EA[0] = atan2(2 * (q[3]*q[0] - q[1]*q[2]),\
                  ((q[0]**2) - (q[1]**2) + (q[2]**2) - (q[3]**2)))
        
    EA[1] = asin(2 * (q[0]*q[1] + q[2]*q[3]))
    
    EA[2] = atan2(2 * (q[2]*q[0] - q[3]*q[1]),\
                  ((q[0]**2) - (q[1]**2) - (q[2]**2) + (q[3]**2)))
    
    return EA


def EA313(values):
    q = value_convert(values)
    
    EA[0] = atan2((q[1]*q[3] + q[2]*q[0]), -(q[2]*q[3] - q[1]*q[0]))
    EA[1] = acos((q[0]**2) - (q[1]**2) - (q[2]**2) + (q[3]**2))
    EA[2] = atan2((q[1]*q[3] - q[2]*q[0]), (q[2]*q[3] + q[1]*q[0]))
    
    return EA


def EA321(values):
    q = value_convert(values)
    
    EA[0] = atan2(2 * (q[1]*q[2] + q[3]*q[0]),\
                  ((q[0]**2) + (q[1]**2) - (q[2]**2) - (q[3]**2)))
    
    if (2 * (q[0]*q[2] - q[1]*q[3])) > 1:
        EA[1] = asin(1)
        
    elif (2 * (q[0]*q[2] - q[1]*q[3])) < -1:
        EA[1] = asin(-1)
        
    else:
        EA[1] = asin(-2*(q[1]*q[3] - q[0]*q[2]))
    
    EA[2] = atan2(2 * (q[1]*q[0] + q[3]*q[2]),\
                  ((q[0]**2) - (q[1]**2) - (q[2]**2) + (q[3]**2)))
    
    return EA

def EA323(values):
    q = value_convert(values)
    
    EA[0] = atan2((q[2]*q[3] - q[0]*q[1]), (q[1]*q[3] + q[2]*q[0]))
    
    if ((q[0]**2) - (q[1]**2) - (q[2]**2) + (q[3]**2)) > 1:
        EA[1] = acos(1)
        
    elif ((q[0]**2) - (q[1]**2) - (q[2]**2) + (q[3]**2)) < -1:
        EA[1] = acos(-1)
    
    else:
        EA[1] = acos((q[0]**2) - (q[1]**2) - (q[2]**2) + (q[3]**2))
        
    EA[2] = atan2((q[0]*q[1] + q[2]*q[3]), (q[2]*q[0] - q[1]*q[3]))
    
    return EA