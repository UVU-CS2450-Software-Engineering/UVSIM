import customtkinter as ctk

class IOWidgets(ctk.CTkFrame):
    def __init__(self, vm, master) -> None:
        # Create frame and sub-widgets
        super().__init__(master)
        self.input_label = ctk.CTkLabel(master=self, text='Input')
        self.input_entry = ctk.CTkEntry(master=self, width=125)
        self.input_button = ctk.CTkButton(master=self, text='Submit', width=75, command=self.set_output)

        self.output_label = ctk.CTkLabel(master=self, text='Output')
        self.output_text_box = ctk.CTkTextbox(master=self, yscrollcommand=True, state='disabled', width=200, height=75)

        self.accumulator_label = ctk.CTkLabel(master=self, text='Accumulator Value')
        self.accumulator_text_box = ctk.CTkTextbox(master=self, yscrollcommand=True, state='disabled', width=200, height=25)


        # Pack sub-widgets in frame using grid
        self.input_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='nw')
        self.input_entry.grid(row=2, column=0, padx=(10, 1), pady=(0, 5), sticky='nw', columnspan=2)
        self.input_button.grid(row=2, column=2, padx=(1, 10), pady=(0, 5), sticky='nw')
        
        self.output_label.grid(row=3, column=0, padx=10, pady=(5, 0), sticky='nw')
        self.output_text_box.grid(row=4, column=0, padx=10, pady=(0, 5), sticky='nw', columnspan=3)

        self.accumulator_label.grid(row=5, column=0, padx=10, pady=(5, 0), sticky='nw')
        self.accumulator_text_box.grid(row=6, column=0, padx=10, pady=(0, 5), sticky='nw', columnspan=3)

    def get_input(self):
        user_input = self.input_entry.get()
        return user_input
    
    def set_output(self):
        self.output_text_box.configure(state='normal')
        # need to get output from vm
        self.output_text_box.insert('current', 'instruction\n')
        self.output_text_box.configure(state='disabled')
        self.update_accumulator()

    def update_accumulator(self):
        self.accumulator_text_box.configure(state='normal')
        self.accumulator_text_box.delete('current', 'end')
        # need to get accumulator value from vm
        self.accumulator_text_box.insert('current', 'acc value')
        self.accumulator_text_box.configure(state='disabled')
        
        