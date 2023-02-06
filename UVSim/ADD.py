from __future__ import annotations
from instruction import instruction
from virtual_machine import virtual_machine


class add(instruction):
    """
    a class for the add instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name: str = "ADD"
        assert (
            self.op_code == 30
        ), "Tried to create an Add instruction with mismatched op code"

    def exec(self: instruction, vm: virtual_machine):
        """
        take the location from the last two digits (main_memory)
        and add it to the value in the accumulator
        store in the accumulator
        """

        vm.accumulator = vm.main_memory[self.param] + vm.accumulator
