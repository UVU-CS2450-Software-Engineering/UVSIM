import re

def read_ml(path):
    '''Reads in a supplied program file and stores each line as an element in a list'''
    instructions = []
    try:
        with open(path, 'r') as prgm:
            instruction = prgm.readline().strip()
            while instruction:
                print(len(instructions))
                if len(instructions) > 100:
                    raise BufferError('Memory Overflow: Too many lines in program.')
                # Regex to validate format
                if not re.search("^((\+|-)\d{4})$", instruction):
                    raise ValueError(f'Invalid word at line: {len(instructions) + 1}')
                instructions.append(instruction)
                instruction = prgm.readline().strip()
        return instructions
    except BufferError as e:
        print(e)
        return False
    except OSError:
        print(f'Unable to open file at: {path}')
        return False
    except ValueError as e:
        print(e)
        return False

