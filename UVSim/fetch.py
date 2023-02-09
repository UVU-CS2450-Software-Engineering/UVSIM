from UVSim.vm import virtualMachine


def fetch(vm: virtualMachine) -> str:
    """
    given the vm fetch the next instruction and return it
    as a string
    format +/-####
    increment the next instruction (so it grabs a new one every time)
    If branch changes the instruction pointer that should be fine too.
    """
    assert (
        vm.nextInstruction >= 0 and vm.nextInstruction <= 99
    ), "tried to fetch out of bounds of main_memory"
    return_str: str = vm.mainMemory[vm.nextInstruction]
    vm.nextInstruction += 1
    return return_str
