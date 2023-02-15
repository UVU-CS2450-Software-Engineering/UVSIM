from UVSim.vm_operations import *

# Import remaining instructions
# TODO: subtract
# TODO: divide
# TODO: multiply
# TODO: branch
# TODO: branch_neg
# TODO: branch_zero
# TODO: halt


def decode(instr_str: str) -> instruction:
    """
    given an instruction string return the proper child class of instruction
    """
    op_code = int(instr_str[1:3])
    my_instruction: instruction = None
    if op_code == 10:
        # read instruction
        my_instruction = read(instr_str)
        pass
    elif op_code == 11:
        # write instruction
        my_instruction = write(instr_str)
        pass
    elif op_code == 20:
        # load instruction
        my_instruction = load(instr_str)
        pass
    elif op_code == 21:
        # store instruction
        my_instruction = store(instr_str)
        pass
    elif op_code == 30:
        # add instruction
        my_instruction = add(instr_str)
        pass
    elif op_code == 31:
        # subtract instruction
        my_instruction = subtract(instr_str)
        pass
    elif op_code == 32:
        # divide instruction
        my_instruction = divide(instr_str)
        pass
    elif op_code == 33:
        # multiply instruction
        my_instruction = multiply(instr_str)
        pass
    elif op_code == 40:
        # Branch unconditional instruction
        my_instruction = branch(instr_str)
        pass
    elif op_code == 41:
        # Branch negative instruction
        my_instruction = branch_neg(instr_str)
        pass
    elif op_code == 42:
        # Branch zero instruction
        my_instruction = branch_zero(instr_str)
        pass
    elif op_code == 43:
        # halt instruction
        my_instruction = halt(instr_str)
        pass
    else:
        raise Exception(
            "tried to decode an instruction with an opcode outside the architecture"
        )
    return my_instruction
