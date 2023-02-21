# from UVSim import *

import customtkinter as ctk

from memory_interface import MemoryInterface

class SimGui(ctk.CTk):
    def __init__(self):
        super().__init__()

        # self.v_machine = vm.virtualMachine()
        self.program_file = None

        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('dark-blue')

        self.title('UVSim')
        self.geometry('500x500')

        # File Load Widget Group


        # Memory Widget Group
        self.memory = MemoryInterface(master=self)
        self.memory.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')


        # IO Widget Group

        # Run widget

        # Reset Widget
        
        # Replace with load file functionality
        


        # Everything must initialize prior to this line
        self.mainloop()


if __name__ == '__main__':
    SimGui()
