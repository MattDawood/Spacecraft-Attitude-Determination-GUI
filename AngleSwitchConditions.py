# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 23:09:57 2021

@author: Matthew
"""
from tkinter.messagebox import showerror
import numpy as np
import sys
# Create import path from seperate folder
sys.path.insert(1, "C:\\Users\\Matthew\\Desktop\\Python Projects\\SAD GUI\\Cases")

import EAtoDCM, EAtoEP, DCMtoEA, EPtoEA

# (Global Lists)
# Parameterization Options
parameters = ["Euler Angles ==> Direction Cosine Matrix",
              "Euler Angles ==> Euler Parameters",
              "Direction Cosine Matrix  ==> Euler Angles",
              "Euler Parameters ==> Euler Angles"]

def angle_switch(curr_seq: str, parameter: str, values: list, unit: str) -> list:
    """
    Takes in Angle Sequence, Current Parameter, list of Values, & selected 
    unit and calls appropreaite transformation.
    
    Returns
    -------
        List of values that have been transformed.

    """
    def convert_unit(returned_values, unit):
        for i in range(len(returned_values)):
            returned_values[i] = np.rad2deg(returned_values[i])
                
        return returned_values
    
    try:
    
        if curr_seq == '121':
            if parameter == parameters[0]:
                return EAtoDCM.DCM121(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP121(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA121(values), unit)
                    
                else:
                    return DCMtoEA.EA121(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA121(values), unit)
                
                else:
                    return EPtoEA.EA121(values)
            
        elif curr_seq == '123':
            if parameter == parameters[0]:
                return EAtoDCM.DCM123(values, unit)
            
            elif parameter == parameters[1]:
               return EAtoEP.EP123(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA123(values), unit)
                
                else:
                    return DCMtoEA.EA123(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA123(values), unit)
                    
                else:
                    return EPtoEA.EA123(values)
            
        elif curr_seq == '131':
            if parameter == parameters[0]:
                return EAtoDCM.DCM131(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP131(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA131(values), unit)
                else:
                    return DCMtoEA.EA131(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA131(values), unit)
                
                else:
                    return EPtoEA.EA131(values)
                
        elif curr_seq == '132':
            if parameter == parameters[0]:
                return EAtoDCM.DCM132(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP132(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA132(values), unit)
                    
                else:
                    return DCMtoEA.EA132(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA132(values), unit)
                    
                else:
                    return EPtoEA.EA132(values)
        
        elif curr_seq == '212':
            if parameter == parameters[0]:
                return EAtoDCM.DCM212(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP212(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA212(values), unit)
                
                else:
                    return DCMtoEA.EA212(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA212(values), unit)
                
                else:
                    return EPtoEA.EA212(values)
            
        elif curr_seq == '213':
            if parameter == parameters[0]:
                return EAtoDCM.DCM213(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP213(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA213(values), unit)
                
                else:
                    return DCMtoEA.EA213(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA213(values), unit)
                
                else:
                    return EPtoEA.EA213(values)
            
        elif curr_seq == '231':
            if parameter == parameters[0]:
                return EAtoDCM.DCM231(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP231(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA231(values), unit)
                
                else:
                    return DCMtoEA.EA231(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA231(values), unit)
                
                else:
                    return EPtoEA.EA231(values)
            
        elif curr_seq == '232':
            if parameter == parameters[0]:
                return EAtoDCM.DCM232(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP232(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA232(values), unit)
                
                else:
                    return DCMtoEA.EA232(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA232(values), unit)
                
                else:
                    return EPtoEA.EA232(values)
            
        elif curr_seq == '312':
            if parameter == parameters[0]:
                return EAtoDCM.DCM312(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP312(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA312(values), unit)
                
                else:
                    return DCMtoEA.EA312(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA312(values), unit)
                
                else:
                    return EPtoEA.EA312(values)
            
        elif curr_seq == '313':
            if parameter == parameters[0]:
                return EAtoDCM.DCM313(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP313(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA313(values), unit)
                
                else:
                    return DCMtoEA.EA313(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA313(values), unit)
                
                else:
                    return EPtoEA.EA313(values)
            
        elif curr_seq == '321':
            if parameter == parameters[0]:
               return EAtoDCM.DCM321(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP321(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA321(values), unit)
                    
                else:
                    return DCMtoEA.EA321(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA321(values), unit)
                
                else:
                    return EPtoEA.EA321(values)
            
        elif curr_seq == '323':
            if parameter == parameters[0]:
                return EAtoDCM.DCM323(values, unit)
            
            elif parameter == parameters[1]:
                return EAtoEP.EP323(values, unit)
            
            elif parameter == parameters[2]:
                if unit == "Degrees":
                    return convert_unit(DCMtoEA.EA323(values), unit)
                
                else:
                    return DCMtoEA.EA323(values)
            
            elif parameter == parameters[3]:
                if unit == "Degrees":
                    return convert_unit(EPtoEA.EA323(values), unit)
                
                else:
                    return EPtoEA.EA323(values)
                
    except ValueError:
        showerror(title="Value Error", message="Ensure all inputs are valid.")
        