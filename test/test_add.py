# Cannot test add until VM class is done.
import pytest

from UVSim.ADD import add
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine, accumulator, nextInstruction


def test_add():
    """
    test functionality of the add instruction
    """

    # This instruction says add the value at memory location 0 (which is 100)
    # To the accumulator. The result should be 100
    my_instr: str = "+3000"
    main_memory = list(range(100))
    main_memory[0] = "+0100"
    my_inst: instruction = add(instr=my_instr)
    assert str(my_inst) == "instruction:+3000 op_code:30 param:0 name:ADD"

    # initialize the virtual machine
    my_accumulator: accumulator = accumulator()
    my_nextInstruction: nextInstruction = nextInstruction()
    my_vm: virtualMachine = virtualMachine(my_accumulator)
    my_vm.mainMemory = main_memory
    my_vm.vmAccumulator = my_accumulator
    my_vm.nextInstruction = my_nextInstruction

    my_inst.exec(my_vm)

    assert my_vm.vmAccumulator.value == 100

    # This instruction means add the value stored at memory location 1
    # To the accumulator (100 + -101) the result should be -1
    main_memory[1] = "-0101"
    my_inst = add("+3001")
    my_inst.exec(my_vm)
    print(my_vm.vmAccumulator.value)
    assert my_vm.vmAccumulator.value == -1


def test_add_errors():
    # This should throw an error becuase of wrong opcode
    with pytest.raises(Exception):
        my_instruction: instruction = add("+3100")


def main():
    """
    quick testing main
    """
    test_add()


if __name__ == "__main__":
    main()
