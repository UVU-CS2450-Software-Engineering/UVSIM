import pytest

from UVSim.BRANCHNEG import branch_neg
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

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
