from __future__ import annotations
from abc import ABC, abstractmethod
from virtual_machine import virtual_machine

class instruction(ABC):
  """
  op_name:str
  param:int
  instr:int
  """
  @abstractmethod
  def __init__(self:instruction,instr:int)->None:
    """
    the constructor
    """
    self.instr:int = instr

  @abstractmethod
  def exec(self:instruction, vm:virtual_machine):
    """
    defined by the child, do whatever the instruction does
    """
    pass