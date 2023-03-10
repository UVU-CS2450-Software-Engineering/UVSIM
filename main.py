import sys

from UVSim.read_ml import read_ml
from UVSim.vm import virtualMachine
from UVSim.fetch import fetch
from UVSim.decode import decode


def displayError(e):
    print(e)
    sys.exit()


def main():
    """
    main runner
    """
    vm = virtualMachine()

    program_path = input("Enter program path to run: ")

    memory = read_ml(program_path)
    if "result" in memory.keys():
        vm.mainMemory = memory["result"]

    else:
        displayError(f'Error: {memory["error"]}')

    while not vm.exit:
        while not vm.awaitInput and not vm.exit:
            try:
                mem_val = fetch(vm)
                instruction = decode(mem_val)
                val = instruction.exec(vm)
                if val:
                    print(val)
            except Exception as e:
                displayError(e)
        if vm.awaitInput:
            value = input("Enter a word to read to memory: ")
            vm.reader.validateInput(vm, value)


if __name__ == "__main__":
    main()
