from __future__ import annotations
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine
from UVSim.util import interpret_as_int


class subtract(instruction):
    """
    a class for the subtract instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name: str = "SUBTRACT"
        assert (
            self.op_code == 31
        ), "Tried to create an subtract  instruction with mismatched op code"

    def exec(self: instruction, vm: virtualMachine):
        """
        take the accumulator 
        and subtract it by the last two digits (main_memory)
        store in the accumulator
        """

        vm.vmAccumulator = (
            vm.vmAccumulator - interpret_as_int(vm.mainMemory[self.param])
        )
