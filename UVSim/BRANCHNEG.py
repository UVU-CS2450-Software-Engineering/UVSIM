from __future__ import annotations
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

class branchneg(instruction):
    """
    a class for the branchneg instruction
    """
    def __init__(self: instruction, instr: str) -> None:
        super().__init__(instr)
        self.op_name: str = "BRANCHNEG"
        assert (
            self.op_code == 41
        ), "Tried to create an branchneg instruction with mismatched op code"

    def exec(self: instruction, vm: virtualMachine):
        """
        Check if the accumulator is negative. If so set the 
        nextInstruction pointer to the arguement passed in param
        """
        if vm.vmAccumulator < 0:
            vm.nextInstruction = self.param
