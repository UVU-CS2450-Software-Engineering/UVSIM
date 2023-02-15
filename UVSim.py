'''
Driver for UVSim package
Usage: python -m UVSim
'''

import sys

from UVSim import *

def displayError(e):
    print(e)
    sys.exit()

vm = vm.virtualMachine()

program_path = input('Enter program path to run: ')

memory = read_ml.read_ml(program_path)
if 'result' in memory.keys():
    vm.mainMemory = memory['result']

else:
    displayError(f'Error: {memory["error"]}')

while not vm.exit:
    while not vm.awaitInput:
        try:
            mem_val = fetch(vm)
            instruction = decode(mem_val)
            instruction.exec(vm)
        except Exception as e:
            displayError(e)
    value = input("Enter a word to read to memory: ")
    vm.reader.validateInput(vm, value)

print('Program complete. Press any key to continue...')
input()
