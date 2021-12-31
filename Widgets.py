# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:50:56 2021

@author: Matthew
"""
import tkinter as tk
#from SpacecraftAttitudeDeterminationGUI import add_units_option

# (Global Variables) Adds default text font and size to variable
label_font = ('Times New Roman', 22)
text_font  = ('Times New Roman', 12)
other_font = ('Times New Roman', 18)

# (Global Lists)

# Parameterization Options
parameters = ["Euler Angles ==> Direction Cosine Matrix",
              "Euler Angles ==> Euler Parameters",
              "Direction Cosine Matrix  ==> Euler Angles",
              "Euler Parameters ==> Euler Angles",
              "Euler Parameters ==> Direction Cosine Matrix",
              "Direction Cosine Matrix ==> Euler Parameters",
              "Euler Parameters ==> Gibbs Vector",
              "Gibbs Vector ==> Euler Parameters",
              "Direction Cosine Matrix ==> Gibbs Vector",
              "Gibbs Vector ==> Direction Cosine Matrix",
              "Direction Cosine Matrix ==> Principal Rotation Vector, Q",
              "Principal Rotation Vector, Q ==> Direction Cosine Matrix",
              "Direction Cosine Matrix ==> Modified Rodrigues Parameters",
              "Modified Rodrigues Parameters ==> Direction Cosine Matrix"]
    
# Angle Sequence Optioins
sequences = ["121", "123", "131", "132", 
             "212", "213", "231", "232",
             "312", "313", "321", "323"]

# Radian / Degree
units = ["Radians", "Degrees"]

def add_units_option(app):
    """
    Adds unit option menu to GUI.
    """
    unit = tk.StringVar()
    unit.set(units[0])
    
    unit_choice = tk.OptionMenu(app, unit, *units)
    unit_choice.grid(row=1, column=4, pady=(0,25), sticky='nw')
    unit_choice.config(width=7)
    
    def check_unit_change(*args):
        remove_unit_result(app)
    
    # Handels Changes in Unit Menu
    unit.trace('w', check_unit_change)
        
    return unit

def remove_unit_result(app):
    """
    Clears label when unit is changed to make room for new values
    """
    for x in app.grid_slaves():
        if int(x.grid_info()["row"]) > 1 and int(x.grid_info()["row"]) < 14:
            if int(x.grid_info()["column"]) > 16:
                x.grid_forget()


def add_angle_entry_widgets(app):
    """
    Creates labels and entry widgets for Euler Angle entries and adds unit 
    choice, either radians or degrees
    """
    tk.Label(app, text='α₁:', font=label_font).grid(row=2, column=0)
    tk.Label(app, text='β₂:', font=label_font).grid(row=3, column=0)
    tk.Label(app, text='γ₃:', font=label_font).grid(row=4, column=0)
    
    add_units_option(app)
    
    α = tk.StringVar()
    β = tk.StringVar()
    γ = tk.StringVar()
    
    α_input = tk.Entry(app, borderwidth=3, relief="sunken", textvariable=α,
                       font= text_font, width=7, justify="center")
    α_input.grid(row=2, column=1, sticky='w')
    
    β_input = tk.Entry(app, borderwidth=3, relief="sunken", textvariable=β,
                       font= text_font, width=7, justify="center")
    β_input.grid(row=3, column=1, sticky='w')
    
    γ_input = tk.Entry(app, borderwidth=3, relief="sunken", textvariable=γ,
                       font= text_font, width=7, justify="center")
    γ_input.grid(row=4, column=1, sticky='w')
    
    return [α, β, γ]

def add_DCM_Entry_widgets(app):
    """
    Creates entry widgets for a 3x3 direct cosine matrix
    """
    DCM_matrix = {}
    
    for row in range(3):
        for col in range(3):
            # Single out last row for padding reasons
            if row == 3:
                DCM_matrix["a{}{}".format(row,col)] = tk.StringVar()
            
                tk.Entry(app, borderwidth=3, relief="sunken", font=text_font, 
                         textvariable= DCM_matrix["a{}{}".format(row,col)],
                         width=7, justify="center")\
                        .grid(row=row+2, column=col)
            else:
                DCM_matrix["a{}{}".format(row,col)] = tk.StringVar()
                
                tk.Entry(app, borderwidth=3, relief="sunken", font=text_font, 
                         textvariable= DCM_matrix["a{}{}".format(row,col)],
                         width=7, justify="center")\
                        .grid(row=row+2, column=col, pady=(0,25))
                
    return DCM_matrix

def add_EP_entry_widgets(app, parameter: str):
    """
    Creates labels and entry widgets for Euler Parameter entries
    """
    tk.Label(app, text='e₀:', font=label_font).grid(row=2, column=0,sticky="n")       
    tk.Label(app, text='e₁:', font=label_font).grid(row=3, column=0,sticky="n")   
    tk.Label(app, text='e₂:', font=label_font).grid(row=4, column=0,sticky="n")        
    tk.Label(app, text='e₃:', font=label_font).grid(row=5, column=0, sticky="s")
    
    param0 = tk.StringVar()
    param1 = tk.StringVar()
    param2 = tk.StringVar()
    param3 = tk.StringVar()
    
    param0_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=param0,font= text_font, width=8, 
                            justify="center")
    param0_entry.grid(row=2, column=1, sticky='w')
    
    param1_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=param1,font= text_font, width=8, 
                            justify="center")
    param1_entry.grid(row=3, column=1, sticky='w')
    
    param2_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=param2,font= text_font, width=8, 
                            justify="center")
    param2_entry.grid(row=4, column=1, sticky='w')
    
    param3_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=param3,font= text_font, width=8, 
                            justify="center")
    param3_entry.grid(row=5, column=1, sticky='w')

    return  [param0, param1, param2, param3]

def add_Gibbs_entry_widgets(app):
    """
    Creates labels and entry widgets for Gibbs Vector entries
    """
    tk.Label(app, text='G1:', font=label_font).grid(row=2, column=0)
    tk.Label(app, text='G2:', font=label_font).grid(row=3, column=0)
    tk.Label(app, text='G3:', font=label_font).grid(row=4, column=0)
    
    Gibbs_1 = tk.StringVar()
    Gibbs_2 = tk.StringVar()
    Gibbs_3 = tk.StringVar()
    
    Gibbs1_input = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=Gibbs_1, font= text_font, width=7, 
                            justify="center")
    Gibbs1_input.grid(row=2, column=1, sticky='w')
    
    Gibbs2_input = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=Gibbs_2,font= text_font, width=7, 
                            justify="center")
    Gibbs2_input.grid(row=3, column=1, sticky='w')
    
    Gibbs3_input = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=Gibbs_3, font= text_font, width=7, 
                            justify="center")
    Gibbs3_input.grid(row=4, column=1, sticky='w')
    
    return [Gibbs_1, Gibbs_2, Gibbs_3]

def add_MRP_entry_widgets(app):
    """
    Creates labels and entry widgets for Gibbs Vector entries
    """      
    tk.Label(app, text='σ₁:', font=label_font).grid(row=2, column=0,sticky="n")   
    tk.Label(app, text='σ₂:', font=label_font).grid(row=3, column=0,sticky="n")        
    tk.Label(app, text='σ₃:', font=label_font).grid(row=4, column=0, sticky="s")
    tk.Label(app, text='ξ:', font=label_font).grid(row=5, column=0,sticky="n") 
    
    σ1 = tk.StringVar()
    σ2 = tk.StringVar()
    σ3 = tk.StringVar()
    ξ  = tk.StringVar()
    
    σ1_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=σ1, font= text_font, width=8, 
                            justify="center")
    σ1_entry.grid(row=2, column=1, sticky='w')
    
    σ2_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=σ2, font= text_font, width=8, 
                            justify="center")
    σ2_entry.grid(row=3, column=1, sticky='w')
    
    σ3_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=σ3, font= text_font, width=8, 
                            justify="center")
    σ3_entry.grid(row=4, column=1, sticky='w')
    
    ξ_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=ξ, font= text_font, width=8, 
                            justify="center")
    ξ_entry.grid(row=5, column=1, sticky='w')
    
    return [σ1, σ2, σ3, ξ]
    
def add_PRV_entry_widgets(app):
    """
    Creates labels and entry widgets for Principal Rotation Vector entries
    """      
    tk.Label(app, text='PRV₁:', font=label_font).grid(row=2, column=0,sticky="n")   
    tk.Label(app, text='PRV₂:', font=label_font).grid(row=3, column=0,sticky="n")        
    tk.Label(app, text='PRV₃:', font=label_font).grid(row=4, column=0, sticky="s")
    tk.Label(app, text='θ:', font=label_font).grid(row=5, column=0,sticky="n") 
    
    PRV1 = tk.StringVar()
    PRV2 = tk.StringVar()
    PRV3 = tk.StringVar()
    θ    = tk.StringVar()
    
    PRV1_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=PRV1, font= text_font, width=8, 
                            justify="center")
    PRV1_entry.grid(row=2, column=1, sticky='w')
    
    PRV2_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=PRV2, font= text_font, width=8, 
                            justify="center")
    PRV2_entry.grid(row=3, column=1, sticky='w')
    
    PRV3_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=PRV3, font= text_font, width=8, 
                            justify="center")
    PRV3_entry.grid(row=4, column=1, sticky='w')
    
    θ_entry = tk.Entry(app, borderwidth=3, relief="sunken", 
                            textvariable=θ, font= text_font, width=8, 
                            justify="center")
    θ_entry.grid(row=5, column=1, sticky='w')
    
    return [PRV1, PRV2, PRV3, θ]

def add_DCM_field(app, result_matrix):
    """
    Creates labels and entry widgets for Direct Cosine Matrix entries
    """      
    for row in range(3):
        for col in range(3):
            matrix = tk.Label(app,text="{:.4f}".format(result_matrix[row,col]), 
                              font=text_font)
            matrix.grid(row=row+2, column=col+4, padx=(0,7), sticky='sw')
            
def add_EP_field(app, result_matrix):
    
    for row in range(4):
        for col in range(1):
            matrix = tk.Label(app,text="{:.4f}".format(result_matrix[row]), 
                              font=text_font)
            matrix.grid(row=row+2, column=col+6)
    
    tk.Label(app, text='e₀:', font=label_font).grid(row=2, column=5,sticky="n")
    tk.Label(app, text='e₁:', font=label_font).grid(row=3, column=5,sticky="n")
    tk.Label(app, text='e₂:', font=label_font).grid(row=4, column=5,sticky="n")
    tk.Label(app, text='e₃:', font=label_font).grid(row=5, column=5, sticky="s")
    
def add_euler_angle_field(app, result_matrix):
    
    tk.Label(app, text='α₁:',font=label_font).grid(row=2,column=5, sticky='nw')
    tk.Label(app, text='β₂:',font=label_font).grid(row=3,column=5, sticky='w')
    tk.Label(app, text='γ₃:',font=label_font).grid(row=4,column=5, sticky='sw')
    
    
    tk.Label(app, text="{:.3f}".format(result_matrix[0]),\
             font = ('Times New Roman', 15)).grid(row=2,column=6, sticky='nw')
            
    tk.Label(app, text="{:.3f}".format(result_matrix[1]),\
             font = ('Times New Roman', 15)).grid(row=3,column=6, sticky='w')
            
    tk.Label(app, text="{:.3f}".format(result_matrix[2]),\
             font = ('Times New Roman', 15)).grid(row=4,column=6, sticky='sw')

def add_Gibbs_field(app, result_matrix):
    tk.Label(app, text='Gibbs1:', font=label_font).grid(row=2, column=5)
    tk.Label(app, text='Gibbs2:', font=label_font).grid(row=3, column=5)
    tk.Label(app, text='Gibbs3:', font=label_font).grid(row=4, column=5)
    
    tk.Label(app, text="{:.3f}".format(result_matrix[0]),\
             font = ('Times New Roman', 15)).grid(row=2,column=6, sticky='nw')
            
    tk.Label(app, text="{:.3f}".format(result_matrix[1]),\
             font = ('Times New Roman', 15)).grid(row=3,column=6, sticky='w')
            
    tk.Label(app, text="{:.3f}".format(result_matrix[2]),\
             font = ('Times New Roman', 15)).grid(row=4,column=6, sticky='sw')
        
def add_mRP_field(app, result_matrix):       
    tk.Label(app, text='σ₁:', font=other_font).grid(row=2, column=5,sticky="n")   
    tk.Label(app, text='σ₂:', font=other_font).grid(row=3, column=5,sticky="n")        
    tk.Label(app, text='σ₃:', font=other_font).grid(row=4, column=5, sticky="n")
    tk.Label(app, text='ξ:', font=other_font).grid(row=5, column=5,sticky="s")
    
    tk.Label(app, text="{:.3f}".format(result_matrix[0]),\
             font = ('Times New Roman', 15)).grid(row=2,column=6, sticky='nw')
            
    tk.Label(app, text="{:.3f}".format(result_matrix[1]),\
             font = ('Times New Roman', 15)).grid(row=3,column=6, sticky='nw')
            
    tk.Label(app, text="{:.3f}".format(result_matrix[2]),\
             font = ('Times New Roman', 15)).grid(row=4,column=6, sticky='nw')
    
    tk.Label(app, text="{:.3f}".format(result_matrix[3]),\
             font = ('Times New Roman', 15)).grid(row=5,column=6, sticky='sw')

def add_PRV_field(app, result_matrix):
    tk.Label(app, text='PRV₁:', font=other_font).grid(row=2, column=5,sticky="n")   
    tk.Label(app, text='PRV₂:', font=other_font).grid(row=3, column=5,sticky="n")        
    tk.Label(app, text='PRV₃:', font=other_font).grid(row=4, column=5, sticky="n")
    tk.Label(app, text='θ:', font=other_font).grid(row=5, column=5,sticky="s")
    
    tk.Label(app, text="{:.3f}".format(result_matrix[0]),\
             font = ('Times New Roman', 15)).grid(row=2,column=6, sticky='nw')
            
    tk.Label(app, text="{:.3f}".format(result_matrix[1]),\
             font = ('Times New Roman', 15)).grid(row=3,column=6, sticky='nw')
            
    tk.Label(app, text="{:.3f}".format(result_matrix[2]),\
             font = ('Times New Roman', 15)).grid(row=4,column=6, sticky='nw')
    
    tk.Label(app, text="{:.3f}".format(result_matrix[3]),\
             font = ('Times New Roman', 15)).grid(row=5,column=6, sticky='sw')