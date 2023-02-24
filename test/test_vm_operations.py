import pytest

from UVSim.vm_operations import *
from UVSim.vm import virtualMachine

def test_instruction():
    """
    check that instuctions are purely abstract and cannot be instantiated
    """
    with pytest.raises(Exception):
        daves_bad_instruction: instruction = instruction(3000)

def test_branch():
    """
    Test functionality of branch instruction
    """
    # This instruction should set nextInstuction to 9
    my_instr: str = "+4009"
    my_inst: instruction = branch(instr=my_instr)
    assert str(my_inst) == "instruction:+4009 op_code:40 param:9 name:BRANCH"

    # initialize the virtual machine
    my_vm: virtualMachine = virtualMachine()

    my_inst.exec(my_vm)

    assert my_vm.nextInstruction == 9

    # This instruction should set nextInstuction to 25
    my_inst = branch("+4025")
    my_inst.exec(my_vm)
    assert my_vm.nextInstruction == 25

def test_branch_errors():
    # This should throw an error becuase of wrong opcode
    with pytest.raises(Exception):
        my_instruction: instruction = branch("+3000")

def test_branchneg():
    """
    Test functionality of branch instruction
    """
    # This instruction should set nextInstuction to 9
    my_instr: str = "+4109"
    my_inst: instruction = branch_neg(instr=my_instr)
    assert str(my_inst) == "instruction:+4109 op_code:41 param:9 name:BRANCHNEG"

    # initialize the virtual machine
    my_vm: virtualMachine = virtualMachine()
    my_vm.vmAccumulator = -1

    my_inst.exec(my_vm)

    assert my_vm.nextInstruction == 9

    # This instruction should set nextInstuction to 25
    my_inst = branch_neg("+4125")
    my_inst.exec(my_vm)
    assert my_vm.nextInstruction == 25

    # This instruction should not affect nextInstruction because vmAccumulator is positive
    my_inst = branch_neg("+4156")
    my_vm.vmAccumulator = 1
    my_inst.exec(my_vm)
    assert my_vm.nextInstruction ==25

def test_branchneg_errors():
    # This should throw an error becuase of wrong opcode
    with pytest.raises(Exception):
        my_instruction: instruction = branch_neg("+3000")

def test_branchzero():
    """
    Test functionality of branch instruction
    """
    # This instruction should set nextInstuction to 9
    my_instr: str = "+4209"
    my_inst: instruction = branch_zero(instr=my_instr)
    assert str(my_inst) == "instruction:+4209 op_code:42 param:9 name:BRANCHZERO"

    # initialize the virtual machine
    my_vm: virtualMachine = virtualMachine()
    my_vm.vmAccumulator = 0

    my_inst.exec(my_vm)

    assert my_vm.nextInstruction == 9

    # This instruction should not affect nextInstruction because vmAccumulator is positive
    my_inst = branch_zero("+4256")
    my_vm.vmAccumulator = 1
    my_inst.exec(my_vm)
    assert my_vm.nextInstruction == 9

    # This instruction should set nextInstuction to 25
    my_inst = branch_zero("+4225")
    my_vm.vmAccumulator = 0
    my_inst.exec(my_vm)
    assert my_vm.nextInstruction == 25

def test_branchzero_errors():
    # This should throw an error becuase of wrong opcode
    with pytest.raises(Exception):
        my_instruction: instruction = branch_zero("+3000")

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
    my_vm: virtualMachine = virtualMachine()
    my_vm.mainMemory = main_memory

    my_inst.exec(my_vm)

    assert my_vm.vmAccumulator == 100

    # This instruction means add the value stored at memory location 1
    # To the accumulator (100 + -101) the result should be -1
    main_memory[1] = "-0101"
    my_inst = add("+3001")
    my_inst.exec(my_vm)
    print(my_vm.vmAccumulator)
    assert my_vm.vmAccumulator == -1

def test_add_errors():
    # This should throw an error becuase of wrong opcode
    with pytest.raises(Exception):
        my_instruction: instruction = add("+3100")

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
    my_inst.exec(my_vm)
    assert my_vm.vmAccumulator == 1

def test_subtract_errors():
    # This should throw an error becuase of wrong opcode
    with pytest.raises(Exception):
        my_instruction: instruction = subtract("+3000")

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

def test_halt():
    """
    Test functionality of halt instruction
    """
    # This instruction should set my_vm.exit to True
    my_instr: str = "+4300"
    my_inst: instruction = halt(instr=my_instr)
    assert str(my_inst) == "instruction:+4300 op_code:43 param:0 name:HALT"

    # initialize the virtual machine
    my_vm: virtualMachine = virtualMachine()

    assert my_vm.exit == False
    my_inst.exec(my_vm)
    assert my_vm.exit == True

def test_halt_errors():
    # This should throw an error becuase of wrong opcode
    with pytest.raises(Exception):
        my_instruction: instruction = halt("+3000")

def test_write_wrong_opcode():
    obj = virtualMachine()
    with pytest.raises(AssertionError):
        instr = write("+1035")

def test_write_param():
    obj = virtualMachine()
    obj.mainMemory[35] = 75
    instr = write("+1135")
    assert instr.param == 35

def test_read_wrong_opcode():
    obj = virtualMachine()
    with pytest.raises(AssertionError):
        instr = read("+1135")

def test_read_param():
    obj = virtualMachine()
    instr = read("+1035")
    assert instr.param == 35

# def test_read_memory_value(monkeypatch):
#     obj = virtualMachine()
#     instr = read("+1035")
#     monkeypatch.setattr("builtins.input", lambda _: "+5240")
#     instr.exec(obj)
#     assert obj.mainMemory[35] == '+5240'

def test_read_input():
    obj = virtualMachine()
    instr = read('+1035')
    obj.vmAccumulator= 35#vmAccumulator will be set by the GUI // read will only be accessed by the GUI
    obj.reader = instr#this is also set by the GUI because validation is done in the GUI
    instr.exec(obj)
    #assert obj.awaitInput
    obj.reader.validateInput(obj, '27')
    assert obj.mainMemory[35] == '+0027'

def test_read_regex():
    obj = virtualMachine()
    with pytest.raises(ValueError):
        instr = read("mane")

def test_load_accum_value():
    obj = virtualMachine()
    obj.mainMemory[35] = 75
    # create load instruction
    instr = load("+2035")
    # execute load instruction
    instr.exec(obj)
    assert obj.vmAccumulator == 75

def test_load_bad_opcode():
    obj = virtualMachine()
    # create load instruction with write opcode
    with pytest.raises(AssertionError):
        instr = load("+1035")

def test_store_mem_value():
    obj = virtualMachine()
    instr = store('+2135')
    obj.vmAccumulator = 91
    instr.exec(obj)
    assert(obj.mainMemory[35] == '+0091')

def test_store_bad_opcode():
    obj = virtualMachine()
    # create store instruction with write opcode
    with pytest.raises(AssertionError):
        instr = store("+1035")
