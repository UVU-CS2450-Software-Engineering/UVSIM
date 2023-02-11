from UVSim.vm import virtualMachine
from UVSim.io import *
import pytest



def test_write_wrong_opcode():
    obj = virtualMachine()
    with pytest.raises(AssertionError):
        instr = write("+1035")


def test_write_param():
    obj = virtualMachine()
    obj.mainMemory[35] = 75
    instr = write("+1135")
    assert instr.param == 35


def test_write_accum_value():
    obj = virtualMachine()
    obj.mainMemory[35] = 75
    # create write instruction
    instr = write("+1135")
    # execute write instruction
    instr.exec(obj)
    assert obj.vmAccumulator == 75


def test_read_wrong_opcode():
    obj = virtualMachine()
    with pytest.raises(AssertionError):
        instr = read("+1135")


def test_read_param():
    obj = virtualMachine()
    instr = read("+1035")
    assert instr.param == 35


def test_read_accum_value(monkeypatch):
    obj = virtualMachine()
    instr = read("+1035")
    monkeypatch.setattr("builtins.input", lambda _: "+5240")
    instr.exec(obj)
    assert obj.vmAccumulator == 5240


def test_read_memory_value(monkeypatch):
    obj = virtualMachine()
    instr = read("+1035")
    monkeypatch.setattr("builtins.input", lambda _: "+5240")
    instr.exec(obj)
    assert obj.mainMemory[35] == 5240


def test_read_regex():
    obj = virtualMachine()
    with pytest.raises(ValueError):
        instr = read("mane")

def test_load_accum_value():
    obj = virtualMachine()
    obj.mainMemory[35] = 75
    # create load instruction
    instr = load("+2035")
    # execute load instruction
    instr.exec(obj)
    assert obj.vmAccumulator == 75

def test_load_bad_opcode():
    obj = virtualMachine()
    # create load instruction with write opcode
    with pytest.raises(AssertionError):
        instr = load("+1035")

def test_store_mem_value():
    obj = virtualMachine()
    instr = store('+2135')
    obj.vmAccumulator = 91
    instr.exec(obj)
    assert(obj.mainMemory[35] == 91)

def test_load_bad_opcode():
    obj = virtualMachine()
    # create store instruction with write opcode
    with pytest.raises(AssertionError):
        instr = store("+1035")