from UVSim.vm import *
import pytest
# uncomment me after instruction.py changes

# def test_write_wrong_opcode():
#     obj = virtualMachine()
#     with pytest.raises(AssertionError):
#         instr = write('+1035')

# def test_write_param():
#     obj = virtualMachine()
#     obj.mainMemory[35] = 75
#     instr = write('+1135')
#     assert(instr.param == 35)

# def test_write_accum_value():
#     obj = virtualMachine()
#     obj.mainMemory[35] = 75
#     #create write instruction
#     instr = write('+1135')
#     #execute write instruction
#     instr.exec(obj)
#     assert(obj.vmAccumulator == 75)