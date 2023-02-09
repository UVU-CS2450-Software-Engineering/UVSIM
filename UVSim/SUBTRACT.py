from __future__ import annotations # What is this?
from instruction import instruction
from virtual_machine import virtual_machine


class subtract(instruction):
    """
    a class for the subtract instruction
    """

    def __init__(self: instruction, instr: int) -> None: #What's happening here. instr is the 2 digit instruction. What is self: instruction?
        super().__init__(instr) # This is calling instruction constructor
        self.op_name: str = "SUBTRACT"
        assert (
            self.op_code == 31
        ), "Tried to create an subtract  instruction with mismatched op code" # What is this assert statement for and the ,

    def exec(self: instruction, vm: virtual_machine):
        """
        take the location from the last two digits (main_memory)
        and subtract it by the value in the accumulator
        store in the accumulator
        """

        vm.accumulator = vm.accumulator - vm.main_memory[self.param]# Is the accumulator just an int?
