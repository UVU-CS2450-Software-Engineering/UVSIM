import pytest

from UVSim import read_ml

def test_no_file():
    commands = read_ml.read_ml('No file')
    assert commands['error']

def test_dummy_file():
    commands = read_ml.read_ml('test/test1.txt')
    assert len(commands['result']) == 100

def test_invalid_entry():
    commands = read_ml.read_ml('test/testInvalid.txt')
    assert commands['error']

def test_max_program():
    commands = read_ml.read_ml('test/testMax.txt')
    assert len(commands['result']) == 100

def test_overflow():
    commands = read_ml.read_ml('test/testOverflow.txt')
    assert commands['error']