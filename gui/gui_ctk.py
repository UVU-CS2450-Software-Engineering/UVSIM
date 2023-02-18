# from UVSim import *

# from tkinter import *
from tkinter import filedialog
# from tkinter import ttk

import customtkinter as ctk


MAX_PROGRAM_SIZE = 100

class ScrollableLabelInputFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = ctk.StringVar()
        self.label_list = []
        self.entry_list = []

    def add_item(self, item, value=None):
        label = ctk.CTkLabel(self, text=item, width=15, compound='left', padx=5, anchor='w')
        entry = ctk.CTkEntry(self, width=90, height=10)
        if value is not None:
            entry.delete(0, ctk.END)
            entry.insert(0, value)
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky='w')
        entry.grid(row=len(self.entry_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.entry_list.append(entry)

    def remove_item(self, item):
        for label, entry in zip(self.label_list, self.entry_list):
            if item == label.cget('text'):
                label.destroy()
                entry.destroy()
                self.label_list.remove(label)
                self.entry_list.remove(entry)
                return


class SIMGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # self.v_machine = vm.virtualMachine()
        self.program_file = None

        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('dark-blue')

        self.title('UVSim')
        self.geometry('500x500')

        self.load_button = ctk.CTkButton(self, text='Load Program', command=self.open_file)
        self.load_button.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        self.program_path = ctk.CTkEntry(self, width=300)
        self.program_path.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nw')

        self.memory = ScrollableLabelInputFrame(master=self, width=300, command=None, corner_radius=0)
        self.memory.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        for i in range(100):
            self.memory.add_item(f'Loc {i}', '+0000')

        self.mainloop()

    def open_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        program_file = filedialog.askopenfilename(title='Select a program to run', initialdir='.', filetypes=filetypes)
        print(program_file)
        self.program_path.delete(0, ctk.END)
        self.program_path.insert(0, program_file)
        


if __name__ == '__main__':
    interface = SIMGUI()
