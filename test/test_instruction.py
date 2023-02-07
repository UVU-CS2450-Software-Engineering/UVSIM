import pytest

from UVSim.instruction import instruction


def test_instruction():
    """
    check that instuctions are purely abstract and cannot be instantiated
    """
    with pytest.raises(Exception):
        daves_bad_instruction: instruction = instruction(3000)
