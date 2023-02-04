import pytest

from UVSim import read_ml

def test_no_file():
    commands = read_ml.read_ml('No file')
    assert not commands

def test_dummy_file():
    commands = read_ml.read_ml('test/test1.txt')
    assert len(commands) == 11