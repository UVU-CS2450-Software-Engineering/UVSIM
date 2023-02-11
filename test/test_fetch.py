import pytest

from UVSim.vm import virtualMachine
from UVSim.fetch import fetch


def test_fetch():
    """
    initialize a vm with a few instructions and try fetching them
    """
    my_vm: virtualMachine = virtualMachine()
    my_vm.nextInstruction = 0
    my_vm.mainMemory[0] = "+1000"
    my_vm.mainMemory[1] = "-1111"
    my_vm.mainMemory[98] = "+1234"
    my_vm.mainMemory[99] = "-1234"

    result_str: str = fetch(my_vm)
    assert result_str == "+1000"
    result_str: str = fetch(my_vm)
    assert result_str == ("-1111")
    my_vm.nextInstruction = 98
    result_str = fetch(my_vm)
    assert result_str == "+1234"
    result_str = fetch(my_vm)
    assert result_str == "-1234"

    # should fail to fetch an instruction outside of main_memory
    my_vm.nextInstruction = -1
    with pytest.raises(Exception):
        fetch(my_vm)
