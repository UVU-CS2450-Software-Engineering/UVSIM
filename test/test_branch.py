import pytest

from UVSim.BRANCH import branch
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

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