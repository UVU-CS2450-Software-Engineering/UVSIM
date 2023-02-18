# from UVSim import *

from tkinter import *
from tkinter import filedialog
from tkinter import ttk


MAX_PROGRAM_SIZE = 100

class SIMGUI:
    def __init__(self):
        # self.v_machine = vm.virtualMachine()
        self.program_file = None

        self.root = Tk()
        self.root.title('UVSim')
        self.root.geometry('500x500')

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open', command=self.open)
        filemenu.add_separator()
        filemenu.add_command(label='Quit', command=self.root.destroy)
        menubar.add_cascade(label='File', menu=filemenu)
        self.root.config(menu=menubar)
        

        frame = ttk.Frame(self.root, padding=10)
        frame.grid()

        ttk.Label(frame, text='Hello World').grid(column=0, row=0)
        ttk.Button(frame, text='Quit', command=self.root.destroy).grid(column=1, row=0)


        def myFunction(event):
            canvas.configure(scrollregion=canvas.bbox('all'), width=400, height=200)

        my_frame = ttk.Frame(self.root, padding=20)
        my_frame.place(x=10, y=10)

        canvas = Canvas(my_frame)
        new_frame = Frame(canvas)
        v_scroll = Scrollbar(my_frame, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(side='right', fill='y')
        canvas.pack(side='left')
        canvas.create_window((0,0), window=new_frame, anchor='nw')
        new_frame.bind('<Configure>', myFunction)

        ttk.Label(new_frame, text='Program').grid(column=0, row=0, columnspan=2)
        for i in range(MAX_PROGRAM_SIZE):
            row = i + 1
            mem_loc = Label(new_frame, text=f'Loc {i}', width=10, font=('Arial', 16))
            mem_loc.grid(row=row, column=0)
            mem_val = Label(new_frame, text=f'Mem Val {i}', width=10, font=('Arial', 16, 'italic'))
            mem_val.grid(row=row, column=1)

        # v.config(command=program_frame.yview)

        self.root.mainloop()

    # def run_gui(self):
    #     self.root.mainloop()

    def open(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        self.program_file = filedialog.askopenfilename(title='Select a program to run', initialdir='.', filetypes=filetypes)
        print(self.program_file)


if __name__ == '__main__':
    interface = SIMGUI()
    # interface.run_gui()