'''
Driver for UVSim package
Usage: python -m UVSim
'''

import sys

from UVSim import *

def displayError(e):
    print(e)
    sys.exit()

def main():
    v_machine = vm.virtualMachine()

    program_path = input('Enter program path to run: ')

    memory = read_ml.read_ml(program_path)
    if 'result' in memory.keys():
        v_machine.mainMemory = memory['result']

    else:
        displayError(f'Error: {memory["error"]}')

    while not v_machine.exit:
        while not v_machine.awaitInput and not v_machine.exit:
            try:
                mem_val = fetch.fetch(v_machine)
                instruction = decode.decode(mem_val)
                instruction.exec(v_machine)
            except Exception as e:
                displayError(e)
        if v_machine.awaitInput:
            value = input("Enter a word to read to memory: ")
            v_machine.reader.validateInput(v_machine, value)

    print('Program complete. Press any key to continue...')
    input()

if __name__ == '__main__':
    main()
