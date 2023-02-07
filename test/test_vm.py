import sys
import pytest
from UVSim.vm import *


def test_vm_accumulator():
    acc = accumulator()
    obj = virtualMachine(acc)
    assert obj.vmAccumulator.value == 0


def test_vm_default_exit_value():
    acc = accumulator()
    obj = virtualMachine(acc)
    assert obj.exit == False


def test_vm_default_next_instruction_value():
    acc = accumulator()
    obj = virtualMachine(acc)
    assert obj.nextInstruction == None
