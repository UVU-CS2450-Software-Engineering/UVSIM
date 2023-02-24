import os, sys

dirname = os.getcwd()
sys.path.insert(0, f"{dirname}/..")

from UVSim import *

import customtkinter as ctk

from memory_interface import MemoryInterface
from io_widgets import IOWidgets
from file_picker import FilePicker
from run_interface import Run

class SimGui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.v_machine = vm.virtualMachine()
        self.program_file = None

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

        self.title("UVSim")
        self.geometry("500x500")

        # File Load Widget Group

        # Memory Widget Group
        self.memory = MemoryInterface(self.v_machine, master=self)
        self.memory.grid(row=1, column=0, padx=10, pady=10, rowspan=2, sticky="nsew")

        # Test code for evaluating memory interface.
        # instructions = read_ml.read_ml('../test/test3.txt')['result']
        # mem_stack = self.memory.memory_list

        # for index, value in enumerate(instructions):
        #     mem_stack.add_item(index, value)

        # IO Widget Group
        self.io_widgets = IOWidgets(self.v_machine, master=self)
        self.io_widgets.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Run widget
        self.run_control = Run(self, self.execute)
        self.run_control.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

        # Reset Widget

        # Replace with load file functionality
        self.file_picker = FilePicker(master=self)
        self.file_picker.grid(
            row=0, column=0, padx=10, pady=10, columnspan=2, sticky="nsew"
        )

        self.close_button = ctk.CTkButton(self, text='Close', command=self.destroy, width=50, height=25)
        self.close_button.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        # Everything must initialize prior to this line
        self.mainloop()

    def load(self):
        instructions = read_ml.read_ml(self.file_picker.get_selected_file_path())
        if 'error' in instructions.keys():
            # Write out error to IO
            return
        instructions = instructions['result']
        for idx, val in enumerate(instructions):
            self.memory.memory_list.add_item(idx, val)
        self.execute()


# New code for execute and get_value()
    def execute(self):
            while not self.v_machine.awaitInput and not self.v_machine.exit:
                try:
                    mem_val = fetch.fetch(self.v_machine)
                    instruction = decode.decode(mem_val)
                    val = instruction.exec(self.v_machine)
                    self.io_widgets.set_output(f'Return Val: {val}')

                    # val = {'write': value} OR {'store': {'location': INT, 'value': value}}
                    # if val and 'write' in val.keys():
                    #     # modify to handle store and GUI IO
                    #     print(val)
                    # elif val and 'store' in val.key():
                    #     idx = val['store']['index']
                    #     val = val['store']['value']
                    #     self.memory.memory_list.add_item(idx, val)
                    # elif val and 'acc' in val.keys():
                    #     set_accumulator(val)

                except Exception as e:
                    self.io_widgets.set_output(f'Exception: {e}')
            if self.v_machine.exit:
                self.io_widgets.set_output('Program complete.')
            elif self.v_machine.awaitInput:
                self.io_widgets.set_output('Enter a value: ')

    def get_input(self, value):
        try:
            val = self.v_machine.reader.validate(value)
            idx = val['store']['index']
            val = val['store']['value']
            self.memory.memory_list.add_item(idx, val)
            self.execute()
        except Exception as e:
            self.io_widgets.set_output('Invalid input')
            self.io_widgets.set_output('Enter a value: ')




'''
    def load(self):
        instructions = read_ml.read_ml(self.file_picker.get_selected_file_path())
        if 'error' in instructions.keys():
            # Write out error to IO
            return
        instructions = instructions['result']
        for idx, val in enumerate(instructions):
            self.memory.memory_list.add_item(idx, val)

    def execute(self):
        #Run the program
        while not self.vm.exit:
            while not self.vm.awaitInput and not self.vm.exit:
                try:
                    mem_val = fetch.fetch(self.vm)
                    instruction = decode.decode(mem_val)
                    val = instruction.exec(vm)
                    if val:
                        print(val)
                        # self.IO.print/write
                except Exception as e:
                    continue
                    # self.IO print error (e)
            if self.vm.awaitInput:
            #IO indicate awaiting input

            else:
                End program

    def read(self):
        # On IO submit button click
        Validate input
        #value = IO get input from user
        #self.vm.reader.validateInput(self.vm, value)
        trigger self.execute()
        
'''

if __name__ == "__main__":
    SimGui()
