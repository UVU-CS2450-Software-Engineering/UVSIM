from UVSim.instruction import instruction
from UVSim.vm import virtualMachine
import re


class write(instruction):
    """
    a class for the write instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        print(self.op_code)
        self.op_name: str = "WRITE"
        assert (
            self.op_code == 11
        ), "Tried to create a write instruction with mismatched op code"

    # get word from memorylocation, move it into the accumulator, output it to the screen
    def exec(self: instruction, vm: virtualMachine):
        # self.param is location in memory of operand to write
        vm.vmAccumulator = vm.mainMemory[self.param]
        print(vm.vmAccumulator)


class read(instruction):
    """
    a class for the read instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name: str = "READ"
        assert (
            self.op_code == 10
        ), "Tried to create a read instruction with mismatched op code"

    # get word from user, move it into the accumulator, put it in memorylocation
    def exec(self: instruction, vm: virtualMachine):
        # self.param is location in memory of destination to write to
        inp = input("Enter a word to read to memory: ")
        # Regex to validate format
        if not re.search("^((\+|-)?\d{4})$", inp):
            raise ValueError(f"Invalid word")
        vm.vmAccumulator = inp
        vm.mainMemory[self.param] = vm.vmAccumulator
