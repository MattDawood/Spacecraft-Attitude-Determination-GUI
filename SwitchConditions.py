# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:04:40 2021

@author: Matthew
"""
from tkinter.messagebox import showerror
import sys
# Create import path from seperate folder
sys.path.insert(1, "C:\\Users\\Matthew\\Desktop\\Python Projects\\SAD GUI\\Cases")

import EPtoDMC, DCMtoMRP, DCMtoEP, EPtoGibbs, GibbstoEP, DCMtoGibbs, mRPtoDCM,\
       GibbstoDCM, DCMtoPRV, PRVtoDCM

# (Global Lists)
# Parameterization Options
parameters = ["Euler Parameters ==> Direction Cosine Matrix",
              "Direction Cosine Matrix ==> Euler Parameters",
              "Euler Parameters ==> Gibbs Vector",
              "Gibbs Vector ==> Euler Parameters",
              "Direction Cosine Matrix ==> Gibbs Vector",
              "Gibbs Vector ==> Direction Cosine Matrix",
              "Direction Cosine Matrix ==> Principal Rotation Vector, Q",
              "Principal Rotation Vector, Q ==> Direction Cosine Matrix",
              "Direction Cosine Matrix ==> Modified Rodrigues Parameters",
              "Modified Rodrigues Parameters ==> Direction Cosine Matrix"]


def switch(parameter: str, values: list) -> list:
    """
    Takes in Current Parameter & Values then calls appropreaite 
    transformation.
    
    Returns
    -------
        List of values that have been transformed.

    """
    try:
    
        if parameter == parameters[0]:
            return EPtoDMC.DCM(values)
        
        elif parameter == parameters[1]:
            return DCMtoEP.EulerParameters(values)
        
        elif parameter == parameters[2]:
            return EPtoGibbs.GibbsVector(values)
        
        elif parameter == parameters[3]:
            return GibbstoEP.EulerParameters(values)
        
        elif parameter == parameters[4]:
            return DCMtoGibbs.Gibbs(values)
        
        elif parameter == parameters[5]:
            return GibbstoDCM.DCM(values)
        
    except ValueError:
        showerror(title="Value Error", message="Ensure all inputs are valid.")
        
def switch_angle(parameter: str, values: list, unit: str) -> list:
    """
    Takes in Current Parameter, List of Values, & selected Unit and 
    calls appropreaite transformation.
    
    Returns
    -------
        List of values that have been transformed.

    """ 
    try:
        if parameter == parameters[6]:
            return DCMtoPRV.PrincipalRotationVector(values, unit)
        
        elif parameter == parameters[7]:
                return PRVtoDCM.DCM(values, unit)
            
        elif parameter == parameters[8]:
            return DCMtoMRP.ModifiedRodriguesParameters(values, unit)
        
        elif parameter == parameters[9]:
            return mRPtoDCM.DCM(values, unit)
        
    except ValueError:
        showerror(title="Value Error", message="Ensure all inputs are valid.")
