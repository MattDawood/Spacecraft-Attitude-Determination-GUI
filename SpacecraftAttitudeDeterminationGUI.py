# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:02:45 2021

@author: Matthew
"""

import tkinter as tk
from AngleSwitchConditions import angle_switch
from SwitchConditions import switch , switch_angle
from Widgets import add_angle_entry_widgets,add_units_option,add_Gibbs_field,\
                    add_DCM_Entry_widgets, add_EP_entry_widgets,\
                    add_DCM_field, add_EP_field, add_euler_angle_field,\
                    add_Gibbs_entry_widgets, add_MRP_entry_widgets,\
                    add_mRP_field, add_PRV_entry_widgets, add_PRV_field


# (Global Variables) Adds default text font and size to variable
label_font = ('Times New Roman', 22)
text_font  = ('Times New Roman', 12)

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

def main():
    # Intializes tkinter
    SADapp = tk.Tk()
    
    # Initialzies GUI with title and dimension size
    SADapp.title('Spacecraft Attitude Determination')
    SADapp.geometry('695x310')
    
    # Displays Title within GUI
    tk.Label(SADapp, text="Sacecraft Attitude Parameterization Conveter",
             font= ("Times New Roman",28)).grid(row=0, column=0, columnspan=15)
    
    # Creates Options Menu for All Possible Conversions
    curr_para = tk.StringVar()
    curr_para.set('Select Parameterization')
    
    # Adds menu to GUI
    conversion = tk.OptionMenu(SADapp, curr_para, *parameters)
    conversion.grid(row=1, column=0, columnspan=3, sticky='w', pady=(0,25))
    conversion.config(width=55)
    
    # Creates Options Menu for All Possible Sequence Angles
    ang_seq_val = tk.StringVar()
    ang_seq_val.set('121')
    
    # Adds menu to GUI
    angle_sequence = tk.OptionMenu(SADapp, ang_seq_val, *sequences)
    angle_sequence.grid(row=1, column=3, pady=(0,25), sticky='w')
    angle_sequence.config(width=3, state="disabled",bg="grey")
    
    def check_for_parameter(*args):
        """
        Switch condition for all parameter selections.
        """
        # Removes previous widgets
        remove_previous_widgets(SADapp)
        
        # Disables Sequence Options Menus
        angle_sequence.config(width=3, state="disabled",bg="grey")
        
        # Euler Angles ==> Direction Cosine Matrix
        if curr_para.get() == parameters[0]:
            # Enables Sequence OPtions Menu
            angle_sequence.config(state="normal", bg="#F0F0F0")
            # Creates list from user entry
            value_list = add_angle_entry_widgets(SADapp)
            # Adds and saves unit option (Degrees or Radians)
            unit_selection = add_units_option(SADapp)
            
            # Adds Transform button and calculates when pressed
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                     [angle_switch(ang_seq_val.get(),
                                                   curr_para.get(),
                                                   value_list,
                                                   unit_selection.get()), 
                                      add_DCM_field(SADapp, 
                                                    angle_switch(
                                                        ang_seq_val.get(),
                                                        curr_para.get(),
                                                        value_list,
                                                        unit_selection.get()))])
            Transform.grid(row=3, column=2, sticky='w')
        
        # Euler Angles ==> Euler Parameters
        elif curr_para.get() == parameters[1]:
            angle_sequence.config(state="normal", bg="#F0F0F0")
            value_list = add_angle_entry_widgets(SADapp)
            unit_selection = add_units_option(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                     [angle_switch(ang_seq_val.get(),
                                                   curr_para.get(),
                                                   value_list,
                                                   unit_selection.get()), 
                                      add_EP_field(SADapp, 
                                                    angle_switch(
                                                        ang_seq_val.get(),
                                                        curr_para.get(),
                                                        value_list,
                                                        unit_selection.get()))])
            Transform.grid(row=3, column=2, sticky='w')
                
        # Direction Cosine Matrix  ==> Euler Angles
        elif curr_para.get() == parameters[2]:
            angle_sequence.config(state="normal", bg="#F0F0F0")
            value_list = add_DCM_Entry_widgets(SADapp)
            unit_selection = add_units_option(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                     [angle_switch(ang_seq_val.get(),
                                                   curr_para.get(),
                                                   value_list,
                                                   unit_selection.get()), 
                                      add_euler_angle_field(SADapp, 
                                                            angle_switch(
                                                                ang_seq_val.get(),
                                                                curr_para.get(),
                                                                value_list,
                                                                unit_selection.get()))])

            Transform.grid(row=3, column=3, sticky='e')
                
        # Euler Parameters ==> Euler Angles
        elif curr_para.get() == parameters[3]:
            angle_sequence.config(state="normal", bg="#F0F0F0")
            value_list = add_EP_entry_widgets(SADapp, curr_para.get())
            unit_selection = add_units_option(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                     [angle_switch(ang_seq_val.get(),
                                                   curr_para.get(),
                                                   value_list,
                                                   unit_selection.get()), 
                                      add_euler_angle_field(SADapp, 
                                                            angle_switch(
                                                                ang_seq_val.get(),
                                                                curr_para.get(),
                                                                value_list,
                                                                unit_selection.get()))])
            Transform.grid(row=3, column=2, sticky='w')
        
        # Euler Parameters ==> Direction Cosine Matrix
        elif curr_para.get() == parameters[4]:
            value_list = add_EP_entry_widgets(SADapp, curr_para.get())
        
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                     command=lambda: 
                                         [switch(curr_para.get(), value_list),
                                          add_DCM_field(SADapp, 
                                                        switch(curr_para.get(),
                                                                value_list))])
            Transform.grid(row=3, column=2, sticky='w')
         
        # Direction Cosine Matrix ==> Euler Parameters
        elif curr_para.get() == parameters[5]:
            value_list = add_DCM_Entry_widgets(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                     command=lambda: 
                                         [switch(curr_para.get(), value_list),
                                          add_EP_field(SADapp, 
                                                       switch(curr_para.get(),
                                                              value_list))])
            Transform.grid(row=3, column=3, sticky='e')
        
        # Euler Parameters ==> Gibbs Vector        
        elif curr_para.get() == parameters[6]:
            value_list = add_EP_entry_widgets(SADapp, curr_para.get())
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                         [switch(curr_para.get(), value_list),
                                          add_Gibbs_field(SADapp, 
                                                       switch(curr_para.get(),
                                                              value_list))])
            Transform.grid(row=3, column=2, sticky='w')
                
        # Gibbs Vector ==> Euler Parameters
        elif curr_para.get() == parameters[7]:
            value_list = add_Gibbs_entry_widgets(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                         [switch(curr_para.get(), value_list),
                                          add_EP_field(SADapp, 
                                                       switch(curr_para.get(),
                                                              value_list))])
            Transform.grid(row=3, column=2, sticky='w')
                
            
        # Direction Cosine Matrix ==> Gibbs Vector
        elif curr_para.get() == parameters[8]:
            value_list = add_DCM_Entry_widgets(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                         [switch(curr_para.get(), value_list),
                                          add_Gibbs_field(SADapp, 
                                                       switch(curr_para.get(),
                                                              value_list))])
            Transform.grid(row=3, column=3, sticky='e')
            
        # Gibbs Vector ==> Direction Cosine Matrix
        elif curr_para.get() == parameters[9]:  
            value_list = add_Gibbs_entry_widgets(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                         [switch(curr_para.get(), value_list),
                                          add_DCM_field(SADapp, 
                                                       switch(curr_para.get(),
                                                              value_list))])
            Transform.grid(row=3, column=2, sticky='w')

        # Direction Cosine Matrix ==> Principal Rotation Vector, Q
        elif curr_para.get() == parameters[10]:
            value_list = add_DCM_Entry_widgets(SADapp)
            unit_selection = add_units_option(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                         [switch_angle(curr_para.get(), 
                                                       value_list, 
                                                       unit_selection.get()),
                                          add_PRV_field(SADapp, 
                                                       switch_angle(
                                                           curr_para.get(), 
                                                           value_list, 
                                                           unit_selection.get()))])
            Transform.grid(row=3, column=3, sticky='e')
                
        # Principal Rotation Vector, Q ==> Direction Cosine Matrix   
        elif curr_para.get() == parameters[11]:
            value_list = add_PRV_entry_widgets(SADapp)
            unit_selection = add_units_option(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                         [switch_angle(curr_para.get(), 
                                                       value_list, 
                                                       unit_selection.get()),
                                          add_DCM_field(SADapp, 
                                                       switch_angle(
                                                           curr_para.get(), 
                                                           value_list, 
                                                           unit_selection.get()))])
            Transform.grid(row=3, column=2, sticky='w')
        
        # Direction Cosine Matrix ==> Modified Rodrigues Parameters
        elif curr_para.get() == parameters[12]:
            value_list = add_DCM_Entry_widgets(SADapp)
            unit_selection = add_units_option(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                         [switch_angle(curr_para.get(), 
                                                       value_list, 
                                                       unit_selection.get()),
                                          add_mRP_field(SADapp, 
                                                       switch_angle(
                                                           curr_para.get(), 
                                                           value_list, 
                                                           unit_selection.get()))])
            
            Transform.grid(row=3, column=3, sticky='e')
                
        # Modified Rodrigues Parameters ==> Direction Cosine Matrix
        elif curr_para.get() == parameters[13]:
            value_list = add_MRP_entry_widgets(SADapp)
            unit_selection = add_units_option(SADapp)
            
            Transform= tk.Button(SADapp, text="Transform", font=text_font,
                                 command=lambda: 
                                         [switch_angle(curr_para.get(), 
                                                       value_list, 
                                                       unit_selection.get()),
                                          add_DCM_field(SADapp, 
                                                       switch_angle(
                                                           curr_para.get(), 
                                                           value_list, 
                                                           unit_selection.get()))])
            Transform.grid(row=3, column=2, sticky='w')
    
    def check_seq_change(*args):
        remove_sequence_result_widgets(SADapp)

    # Handels Changes in Option Menu
    curr_para.trace('w', check_for_parameter)
    
    # Handels Changes In Sequence Menu
    ang_seq_val.trace('w', check_seq_change)

    SADapp.mainloop()
 

def remove_previous_widgets(app):
    """
    Clears widgets / labels to make room for widegets / labels for the
    selected parameterization entries
    """
    for x in app.grid_slaves():
        if int(x.grid_info()["row"]) > 1 and int(x.grid_info()["row"]) < 10:
            x.grid_forget()
        
        elif int(x.grid_info()["row"]) == 1 and \
             int(x.grid_info()["column"]) == 4:
                 x.grid_forget()
        

def remove_sequence_result_widgets(app):
    """
    Clears widgets / labels to make room for widegets / labels for the
    selected sequence results
    """
    for x in app.grid_slaves():
        if int(x.grid_info()["row"]) > 1 and int(x.grid_info()["row"]) < 10:
            if int(x.grid_info()["column"]) > 3:
                x.grid_forget()
    
                

if __name__ == "__main__":
    main()