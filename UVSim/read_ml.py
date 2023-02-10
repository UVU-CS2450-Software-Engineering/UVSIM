import re
init_word = '+0000'

def read_ml(path):
    '''Reads in a supplied program file and stores each line as an element in a list'''
    instructions = []
    try:
        with open(path, 'r') as prgm:
            instruction = prgm.readline().strip()
            while instruction:
                if len(instructions) > 100:
                    raise BufferError('Memory Overflow: Too many lines in program.')
                # Regex to validate format
                if not re.search("^(([+]|-)\d{4})$", instruction):
                    raise ValueError(f'Invalid word at line: {len(instructions) + 1}')
                instructions.append(instruction)
                instruction = prgm.readline().strip()
        while len(instructions) < 100:
            instructions.append(init_word)
        return {'result': instructions}
    except BufferError as e:
        return {'error': e}
    except OSError:
        return {'error': f'Unable to open path at: {path}'}
    except ValueError as e:
        return {'error': e}

