import pytest

from UVSim.DIVIDE import divide
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine


def test_divide():
    """
    test functionality of the divide instruction
    """
    # This instruction say divide the value in the accumulator (30) by
    # the value in memory location [0] (3). Result should be 10
    my_instr: str = "+3200"
    main_memory = list(range(100))
    main_memory[0] = "+0003"
    my_inst: instruction = divide(instr=my_instr)
    assert str(my_inst) == "instruction:+3200 op_code:32 param:0 name:DIVIDE"

    # initialize the virtual machine
    my_vm: virtualMachine = virtualMachine()
    my_vm.mainMemory = main_memory
    my_vm.vmAccumulator = 30

    my_inst.exec(my_vm)

    assert my_vm.vmAccumulator == 10

    # This instruction divides accumulator value(10) by main_memory[1](-2)
    # Accumulator stores result. Should be -5
    main_memory[1] = "-0002"
    my_inst = divide("+3201")
    my_inst.exec(my_vm)
    assert my_vm.vmAccumulator == -5

    def test_divide_errors():
        # This should throw an error becuase of wrong opcode
        with pytest.raises(Exception):
            my_instruction: instruction = divide("+3000")

