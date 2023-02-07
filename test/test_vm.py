import sys
import pytest
from UVSim.vm import *


def test_vm_accumulator():
    obj = virtualMachine()
    assert obj.vmAccumulator == 0


def test_vm_default_exit_value():
    obj = virtualMachine()
    assert obj.exit == False


def test_vm_default_next_instruction_value():
    obj = virtualMachine()
    assert obj.nextInstruction == None
