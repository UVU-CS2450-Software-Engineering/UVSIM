from __future__ import annotations
import customtkinter as ctk
from tkinter import filedialog



class FilePicker(ctk.CTkFrame):
    """
    For allowing the user to navigate to a .asm file
    """
    def __init__(self, master) -> None:
        super().__init__(master)
        self.text_file = ctk.CTkEntry(master=self, width=300)
        self.text_file.grid(row=0, column=0)

        self.button = ctk.CTkButton(
            master=self, command=self.select_file, text="...", width=30
        )
        self.button.grid(row=0, column=1, padx=10, pady=10)

    def select_file(self):
        """
        function for selecting file
        """
        filetypes = (("text files", "*.txt *.asm"), ("All files", "*.*"))
        program_file = filedialog.askopenfilename(
            title="Select a program to run", initialdir=".", filetypes=filetypes
        )
        self.text_file.delete(0, ctk.END)
        self.text_file.insert(0, program_file)
        # Execute load command

    def get_selected_file_path(self) -> str:
        """
        Return the selected file_path
        """
        return self.text_file.get()
