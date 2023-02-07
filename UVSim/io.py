from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

class write(instruction):
    """
    a class for the write instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name: str = "WRITE"
        assert (
            self.op_code == 11
        ), "Tried to create a write instruction with mismatched op code"
    #get word from memorylocation, move it into the accumulator, output it to the screen
    def exec(self: instruction, vm: virtualMachine):
        #self.param is location in memory of operand to write
        vm.vmAccumulator = vm.mainMemory[self.param]
        print(vm.vmAccumulator)