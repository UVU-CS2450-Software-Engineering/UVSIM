from __future__ import annotations
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine
from UVSim.util import interpret_as_int


class multiply(instruction):
    """
    a class for the multiply instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name: str = "MULTIPLY"
        assert (
            self.op_code == 33
        ), "Tried to create a multiply instruction with mismatched op code"

    def exec(self: instruction, vm: virtualMachine):
        """
        take the location from the last two digits (main_memory)
        and multiply it by the value in the accumulator
        store in the accumulator
        """

        vm.vmAccumulator = (
            interpret_as_int(vm.mainMemory[self.param]) * vm.vmAccumulator
        )
