import customtkinter as ctk


class Run(ctk.CTkFrame):
    def __init__(self, master, command):
        super().__init__(master)
        self.run_button = ctk.CTkButton(self, text='Run', command=command, width=50, height=30)
        self.run_button.grid(row=0, column=0, padx=10, pady=10)