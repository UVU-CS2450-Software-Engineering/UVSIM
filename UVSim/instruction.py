from __future__ import annotations
from abc import ABC, abstractmethod
from UVSim import virtual_machine


class instruction(ABC):
    """
    op_name:str
    param:int
    instr:int
    """

    @abstractmethod
    def __init__(self: instruction, instr: int) -> None:
        """
        the constructor
        """
        self.instr: int = instr
        self.op_code = int(str(instr)[:2])
        self.param = int(str(instr[2:]))
        self.op_name = ""

    @abstractmethod
    def exec(self: instruction, vm: virtual_machine):
        """
        defined by the child, do whatever the instruction does
        """
        pass

    def __str__(self: instruction) -> str:
        """
        overload the string operator for easy printing
        """
        return f"instruction:{self.instr} op_code:{self.op_code} param:{self.param} name:{self.op_name}"
