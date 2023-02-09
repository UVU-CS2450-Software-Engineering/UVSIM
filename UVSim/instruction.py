from __future__ import annotations
from abc import ABC, abstractmethod
from UVSim.vm import virtualMachine


class instruction(ABC):
    """
    op_name:str
    param:int
    instr:int
    """

    @abstractmethod
    def __init__(self: instruction, instr: str) -> None:
        """
        the constructor
        """
        self.instr: str = instr
        # starts at one to remove the + or - characters
        self.op_code: int = int(instr[1:3])
        self.param: int = int(instr[3:])
        self.op_name = ""

    @abstractmethod
    def exec(self: instruction, vm: virtualMachine):
        """
        defined by the child, do whatever the instruction does
        """
        pass

    def __str__(self: instruction) -> str:
        """
        overload the string operator for easy printing
        """
        return f"instruction:{self.instr} op_code:{self.op_code} param:{self.param} name:{self.op_name}"
