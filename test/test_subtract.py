import pytest

from UVSim.SUBTRACT import subtract
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine


def test_subtract():
    """
    test functionality of the subtract instruction
    """
    # This instruction say subtract the value in the accumulator (0) by
    # the value in memory location [0] (100). Result should be -100
    my_instr: str = "+3100"
    main_memory = list(range(100))
    main_memory[0] = "+0100"
    my_inst: instruction = subtract(instr=my_instr)
    assert str(my_inst) == "instruction:+3100 op_code:31 param:0 name:SUBTRACT"

    # initialize the virtual machine
    my_vm: virtualMachine = virtualMachine()
    my_vm.mainMemory = main_memory

    my_inst.exec(my_vm)

    assert my_vm.vmAccumulator == -100

    # This instruction subtracts accumulator value(-100) by main_memory[1](-101)
    # Accumulator stores result. Should be -201
    main_memory[1] = "-0101"
    my_inst = subtract("+3101")
    print(my_vm.vmAccumulator)
    print(my_vm.mainMemory[1])
    my_inst.exec(my_vm)
    print(my_vm.vmAccumulator)
    assert my_vm.vmAccumulator == 1

    def test_subtract_errors():
        # This should throw an error becuase of wrong opcode
        with pytest.raises(Exception):
            my_instruction: instruction = subtract("+3000")

