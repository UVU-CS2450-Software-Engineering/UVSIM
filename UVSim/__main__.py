# Place the code to run the package here

from UVSim.read_ml import read_ml
from UVSim.virtual_machine import VirtualMachine

vm = VirtualMachine()

program_path = input('Enter program path to run: ')

vm.instructions = read_ml(program_path)

while True:
    result = vm.execute()
    # Expected values for result from vm.execute()
    # Successfully completed actions that require no IO - no return statement (or return None)
    # Input required - return {input: True, text: 'Message describing required input: '}
    # Output - return {output: True, text: 'Message/value to be displayed'}
    # Program complete - return {complete: True}
    # Error in execution - return {error: 'Descriptive error message'}

    if result == None: continue
    elif result.input:
        data = input(result.text)
        vm.executeInput(data)
    elif result.output:
        print(result.text)
    elif result.complete:
        print('Program complete. Press any key to continue...')
        input()
        break
    else:
        print(f'Error occurred:\n{result.error}')
        print('-' * 20)
        print('Press any key to continue...')
        input()
        break
