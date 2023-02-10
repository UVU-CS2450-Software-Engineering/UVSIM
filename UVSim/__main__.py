'''
Driver for UVSim package
Usage: python -m UVSim
'''

import sys

from UVSim.read_ml import read_ml
from UVSim.vm import virtualMachine
from UVSim.fetch import fetch
from UVSim.decode import decode

vm = virtualMachine()

program_path = input('Enter program path to run: ')

memory = read_ml(program_path)
if 'result' in memory.keys():
    vm.mainMemory = memory

else:
    print(memory);
    print (f'Error: {memory["error"]}\nPress any key to exit program...')
    input()
    sys.exit()


while True:
    mem_val = fetch(vm)
    decode(mem_val)
    if vm.exit:
        print('Program complete. Press any key to continue...')
        input()
        break
