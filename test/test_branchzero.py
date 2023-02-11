import pytest

from UVSim.BRANCHZERO import branch_zero
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

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
