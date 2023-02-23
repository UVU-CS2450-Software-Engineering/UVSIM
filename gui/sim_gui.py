import os, sys

dirname = os.getcwd()
sys.path.insert(0, f'{dirname}/..')

from UVSim import *

import customtkinter as ctk

from memory_interface import MemoryInterface
from io_widgets import IOWidgets

class SimGui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.v_machine = vm.virtualMachine()
        self.program_file = None

        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('dark-blue')

        self.title('UVSim')
        self.geometry('500x500')

        # File Load Widget Group


        # Memory Widget Group
        self.memory = MemoryInterface(self.v_machine, master=self)
        self.memory.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')

        # Test code for evaluating memory interface.
        # instructions = read_ml.read_ml('../test/test3.txt')['result']
        # mem_stack = self.memory.memory_list

        # for index, value in enumerate(instructions):
        #     mem_stack.add_item(index, value)


        # IO Widget Group
        self.io_widgets = IOWidgets(self.v_machine, master=self)
        self.io_widgets.grid(row=2, column=3, padx=10, pady=10, sticky='nsew')

        # Run widget

        # Reset Widget
        
        # Replace with load file functionality
        


        # Everything must initialize prior to this line
        self.mainloop()



if __name__ == '__main__':
    SimGui()
