from __future__ import annotations
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

class halt(instruction):
    """
    a class for the halt instruction
    """
    def __init__(self: instruction, instr: str) -> None:
        super().__init__(instr)
        self.op_name: str = "HALT"
        assert (
            self.op_code == 43
        ), "Tried to create an halt instruction with mismatched op code"

    def exec(self: instruction, vm: virtualMachine):
        """
        Set the vm.exit bool to True
        """
        vm.exit = True