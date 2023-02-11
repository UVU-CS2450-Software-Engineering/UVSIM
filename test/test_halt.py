import pytest

from UVSim.HALT import halt
from UVSim.instruction import instruction
from UVSim.vm import virtualMachine

def test_branch():
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