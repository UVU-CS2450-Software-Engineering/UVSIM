from __future__ import annotations
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

class branch(instruction):
    """
    a class for the branch instruction
    """
    def __init__(self: instruction, instr: str) -> None:
        super().__init__(instr)
        self.op_name: str = "BRANCH"
        assert (
            self.op_code == 40
        ), "Tried to create an branch instruction with mismatched op code"

    def exec(self: instruction, vm: virtualMachine):
        """
        Set the nextInstruction pointer to the arguement passed in param
        """
        vm.nextInstruction = self.param
