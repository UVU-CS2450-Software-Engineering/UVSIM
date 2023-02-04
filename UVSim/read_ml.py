def read_ml(path):
    '''Reads in a supplied program file and stores each line as an element in a list'''
    instructions = []
    try:
        with open(path, 'r') as prgm:
            instruction = prgm.readline().strip()
            while instruction:
                instructions.append(instruction)
                instruction = prgm.readline().strip()
        return instructions
    except OSError:
        print(f'Unable to open file at: {path}')
        return False
