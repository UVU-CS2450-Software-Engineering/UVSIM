import os, sys

dirname = os.getcwd()
sys.path.insert(0, f"{dirname}/..")

from UVSim import *
import customtkinter as ctk
from gui.memory_interface import MemoryInterface
from gui.io_widgets import IOWidgets
from gui.file_picker import FilePicker
from gui.run_interface import Run
from gui.cr_widgets import CRWidgets


class SimGui(ctk.CTk):
    """Graphical user interface that interacts with the business layer through the MemoryInterface class"""

    def __init__(self):
        super().__init__()

        self.v_machine = vm.virtualMachine()
        self.program_file = None

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

        self.title("UVSim")
        self.geometry("500x450")
        self.resizable(0, 0)

        # File Load Widget Group

        # Memory Widget Group
        self.memory = MemoryInterface(self.v_machine, master=self)
        self.memory.grid(
            row=1, column=0, padx=(10, 0), pady=(0, 10), rowspan=2, sticky="nsew"
        )

        # IO Widget Group
        self.io_widgets = IOWidgets(self.v_machine, master=self)
        self.io_widgets.grid(
            row=1, column=1, columnspan=2, padx=(0, 10), pady=0, sticky="nsew"
        )

        # Run widget
        self.run_control = Run(self, self.load)
        self.run_control.grid(row=0, column=2, padx=(0, 10), pady=(10, 0), sticky="e")

        # Reset Widget
        self.close_reset = CRWidgets(self, self.load)
        self.close_reset.grid(
            row=2, column=1, columnspan=2, padx=(0, 10), pady=(0, 10), sticky="se"
        )

        # Replace with load file functionality
        self.file_picker = FilePicker(master=self)
        self.file_picker.grid(
            row=0, column=0, padx=(10, 0), pady=(10, 0), columnspan=2, sticky="nsew"
        )

        # Everything must initialize prior to this line
        self.mainloop()

    def load(self, run=True):
        # load commands from file
        instructions = read_ml.read_ml(self.file_picker.get_selected_file_path())
        if "error" in instructions.keys():
            # self.io_widgets.set_output(str(instructions['error']))# Write out error to IO
            return
        instructions = instructions["result"]
        for idx, val in enumerate(instructions):
            self.memory.memory_list.add_item(idx, val)
        self.v_machine.reset()

        # Run the program
        if run:
            self.execute()

    def execute(self):
        while not self.v_machine.exit:
            while not self.v_machine.awaitInput and not self.v_machine.exit:
                try:
                    mem_val = fetch.fetch(self.v_machine)
                    instruction = decode.decode(mem_val)
                    val = instruction.exec(self.v_machine)
                    if val:
                        match val["key"]:  # switch statement
                            case "math":
                                self.io_widgets.update_accumulator()
                                break
                            case "write":
                                self.io_widgets.set_output(str(val["value"]))
                                break
                            case "store":
                                self.io_widgets.update_accumulator()  # from the accumulator into memory
                                self.memory.memory_list.add_item(
                                    int(val["memLocation"]), int(val["value"])
                                )  # memoryinterface sets value
                                break
                            case "load":
                                self.io_widgets.update_accumulator()
                                break
                            case default:  # control ops
                                break

                except Exception as e:
                    self.io_widgets.set_output("somethings wrong!")
                    continue
            if self.v_machine.awaitInput:
                # IO indicate awaiting input
                self.io_widgets.set_output("Enter a word to read to memory: ")
                while (
                    self.v_machine.awaitInput
                ):  # infinite loop until we get valid input
                    user_input = (
                        self.io_widgets.get_input()
                    )  # value = IO get input from user
                    try:
                        out = self.v_machine.reader.validateInput(
                            self.v_machine, str(user_input)
                        )
                    except ValueError:
                        self.io_widgets.set_output("Invalid input, try again!")
                self.memory.memory_list.add_item(
                    int(out["memLocation"]), int(out["value"])
                )  # memoryinterface sets value
                self.io_widgets.set_output(
                    ">>>" + str(int(out["value"]))
                )  # output user's input to output box

            elif self.v_machine.exit:
                self.io_widgets.set_output("Program complete.")  # End program


if __name__ == "__main__":
    SimGui()
