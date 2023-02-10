from __future__ import annotations
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine
from UVSim.util import interpret_as_int

class branch(instruction):
    """
    a class for the branch instruction
    """
    def __init__(self: instruction, instr: str) -> None:
        super().__init__(instr)
        self.op_name: STR = "BRANCH"
        assert (
            self.op_code == 40
        ), "Tried to create an divide instruction with mismatched op code"

    def exec(self: instruction, vm: virtualMachine):
        """
        Set the nextInstruction pointer to the arguement passed in param
        """
        vm.nextInstruction = self.param
