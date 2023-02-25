import customtkinter as ctk

class CRWidgets(ctk.CTkFrame):
    def __init__(self, master, command) -> None:
        # Create frame and sub-widgets
        super().__init__(master)

        self.reset_button = ctk.CTkButton(self, text='Reset', command=lambda : command(run=False), width=50, height=30)        
        self.close_button = ctk.CTkButton(self, text='Close', command=master.destroy, width=50, height=30)

        self.reset_button.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.close_button.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')