from __future__ import annotations
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

class branchzero(instruction):
    """
    a class for the branchzero instruction
    """
    def __init__(self: instruction, instr: str) -> None:
        super().__init__(instr)
        self.op_name: str = "BRANCHZERO"
        assert (
            self.op_code == 42
        ), "Tried to create an branchzero instruction with mismatched op code"

    def exec(self: instruction, vm: virtualMachine):
        """
        Check if the accumulator is zero. If so set the 
        nextInstruction pointer to the argument passed in param
        """
        if vm.vmAccumulator == 0:
            vm.nextInstruction = self.param

