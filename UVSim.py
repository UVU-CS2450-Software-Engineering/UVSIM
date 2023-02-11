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
    try:
        mem_val = fetch.fetch(vm)
        instruction = decode.decode(mem_val)
        instruction.exec(vm)
    except Exception as e:
        displayError(e)

print('Program complete. Press any key to continue...')
input()