# Cannot test add until VM class is done.
import pytest

from UVSim.MULTIPLY import multiply
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine


def test_multiply():
    """
    test functionality of the multiply instruction
    """

    # This instruction says multiply the value at memory location 0 (which is 100)
    # by the accumulator(value is 0). The result should be 0
    my_instr: str = "+3300"
    main_memory = list(range(100))
    main_memory[0] = "+0100"
    my_inst: instruction = multiply(instr=my_instr)
    assert str(my_inst) == "instruction:+3300 op_code:33 param:0 name:MULTIPLY"

    # initialize the virtual machine
    my_vm: virtualMachine = virtualMachine()
    my_vm.mainMemory = main_memory

    my_inst.exec(my_vm)

    assert my_vm.vmAccumulator == 0

    # Multiply value in accumulator (6) by value of memory[1](-101)
    # Result should be -606
    my_vm.vmAccumulator = 6
    main_memory[1] = "-0101"
    my_inst = multiply("+3301")
    my_inst.exec(my_vm)
    assert my_vm.vmAccumulator == -606


def test_multiply_errors():
    # This should throw an error because of wrong opcode
    with pytest.raises(Exception):
        my_instruction: instruction = multiply("+3400")
