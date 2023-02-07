from __future__ import annotations
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine
from UVSim.util import interpret_as_int


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

    def exec(self: instruction, vm: virtualMachine):
        """
        take the location from the last two digits (main_memory)
        and add it to the value in the accumulator
        store in the accumulator
        """

        vm.vmAccumulator.value = (
            interpret_as_int(vm.mainMemory[self.param]) + vm.vmAccumulator.value
        )
