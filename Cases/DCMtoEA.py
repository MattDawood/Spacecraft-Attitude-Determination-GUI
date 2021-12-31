# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:24:44 2021

@author: Matthew
"""
import numpy as np
from math import acos, asin, atan2

# Global list initialized as zeros
ea = [0] * 3

def value_convert(values):
    DCM_matrix = np.zeros((3,3))
    for row in range(3):
        for col in range(3):
            for key, val in values.items():
                DCM_matrix[row][col] = float(values.get("a{}{}".format(row,col)).get())
    
    return DCM_matrix

def EA121(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[0][1] , -matrix[0][2])
    ea[1] = acos(matrix[0][0])
    ea[2] = atan2(matrix[1][0] , matrix[2][0])
    
    return ea

def EA123(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(-matrix[2][1] , matrix[2][2])
    ea[1] = asin(matrix[2][0])
    ea[2] = atan2(-matrix[1][0] , matrix[0][0])
    
    return ea


def EA131(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[0][2] , matrix[0][1])
    ea[1] = acos(matrix[0][0])
    ea[2] = atan2(matrix[2][0] , -matrix[1][0])
    
    return ea


def EA132(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[1][2] , matrix[1][1])
    ea[1] = asin(-matrix[1][0])
    ea[2] = atan2(matrix[2][0] , matrix[0][0])

    return ea


def EA212(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[1][0] , matrix[1][2])
    ea[1] = acos(matrix[1][1])
    ea[2] = atan2(matrix[0][1] , -matrix[2][1])
    
    return ea


def EA213(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[2][0] , matrix[2][2])
    ea[1] = asin(-matrix[2][1])
    ea[2] = atan2(matrix[0][1] , matrix[1][1])
    
    return ea


def EA231(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(-matrix[0][2] , matrix[0][0])
    ea[1] = asin(matrix[0][1])
    ea[2] = atan2(-matrix[2][1] , matrix[1][1])  
    
    return ea


def EA232(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[1][2] , -matrix[1][0])
    ea[1] = acos(matrix[1][1])
    ea[2] = atan2(matrix[2][1] , matrix[0][1])
    
    return ea


def EA312(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(-matrix[1][0] , matrix[1][1])
    ea[1] = asin(matrix[1][2])
    ea[2] = atan2(-matrix[0][2] , matrix[2][2])
    
    return ea


def EA313(values):
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[2][0] , -matrix[2][1])
    ea[1] = acos(matrix[2][2])
    ea[2] = atan2(matrix[0][2] , matrix[1][2])
    
    return ea


def EA321(values):
    
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[0][1] , matrix[0][0])
    ea[1] = asin(-matrix[0][2])
    ea[2] = atan2(matrix[1][2] , matrix[2][2])
    
    return ea


def EA323(values):
    
    matrix = value_convert(values)
    
    ea[0] = atan2(matrix[2][1] , matrix[2][0])
    ea[1] = acos(matrix[2][2])
    ea[2] = atan2(matrix[1][2] , -matrix[0][2])
    
    return ea