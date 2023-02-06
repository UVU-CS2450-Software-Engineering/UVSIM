from __future__ import annotations
from instruction import instruction
from virtual_machine import virtual_machine

class add(instruction):
    """
    a class for the add instruction
    """
    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name:str = "ADD"

    def exec(self: instruction, vm: virtual_machine):
        """
        take the location from the last two digits (main_memory)
        and add it to the value in the accumulator
        store in the accumulator
        """
        last_two_digits:int = self.instr % 100
        vm.accumulator = vm.main_memory[last_two_digits] + vm.accumulator