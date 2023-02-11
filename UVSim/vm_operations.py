from __future__ import annotations
from abc import ABC, abstractmethod
import re
from UVSim.vm import virtualMachine
from UVSim.util import interpret_as_int

class instruction(ABC):
    """
    op_name:str
    param:int
    instr:int
    """

    @abstractmethod
    def __init__(self: instruction, instr: str) -> None:
        """
        the constructor
        """
        self.instr: str = instr
        # starts at one to remove the + or - characters
        self.op_code: int = int(instr[1:3])
        self.param: int = int(instr[3:])
        self.op_name = ""

    @abstractmethod
    def exec(self: instruction, vm: virtualMachine):
        """
        defined by the child, do whatever the instruction does
        """
        pass

    def __str__(self: instruction) -> str:
        """
        overload the string operator for easy printing
        """
        return f"instruction:{self.instr} op_code:{self.op_code} param:{self.param} name:{self.op_name}"

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

class branch_neg(instruction):
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

class branch_zero(instruction):
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

class add(instruction):
    """
    a class for the add instruction
    """

    def __init__(self: instruction, instr: str) -> None:
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

        vm.vmAccumulator = (
            interpret_as_int(vm.mainMemory[self.param]) + vm.vmAccumulator
        )

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

class divide(instruction):
    """
    a class for the divide instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name: str = "DIVIDE"
        assert (
            self.op_code == 32
        ), "Tried to create an divide instruction with mismatched op code"

    def exec(self: instruction, vm: virtualMachine):
        """
        take the accumulator 
        and divide it by the last two digits (main_memory)
        store in the accumulator
        """

        vm.vmAccumulator = (
            vm.vmAccumulator / interpret_as_int(vm.mainMemory[self.param])
        )

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
        if not re.search("^(([+]|-)?\d{1,4})$", inp):
            raise ValueError(f"Invalid word")
        vm.vmAccumulator = int(inp)
        vm.mainMemory[self.param] = vm.vmAccumulator

class load(instruction):
    """
    a class for the load instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name: str = "LOAD"
        assert (
            self.op_code == 20
        ), "Tried to create a load instruction with mismatched op code"

    # get word from memorylocation, move it into the accumulator
    def exec(self: instruction, vm: virtualMachine):
        # self.param is location in memory of operand to write
        vm.vmAccumulator = int(vm.mainMemory[self.param])

class store(instruction):
    """
    a class for the store instruction
    """

    def __init__(self: instruction, instr: int) -> None:
        super().__init__(instr)
        self.op_name: str = "STORE"
        assert (
            self.op_code == 21
        ), "Tried to create a store instruction with mismatched op code"

    #Store a word from the accumulator into a specific location in memory.
    def exec(self: instruction, vm: virtualMachine):
        # self.param is location in memory of destination
        sign = '+' if vm.vmAccumulator >= 0 else '-'
        vm.mainMemory[self.param] = f'{sign}{vm.vmAccumulator:0>4}'