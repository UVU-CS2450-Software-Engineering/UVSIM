import pytest

from UVSim.decode import decode
from UVSim.instruction import instruction
from UVSim.ADD import add
from UVSim.io import read, write


def test_decode():
    """
    check that existing functions can be decoded correctly
    """
    result_str: str = ""
    result_str = str(decode("+3000"))
    assert result_str == "instruction:+3000 op_code:30 param:0 name:ADD"
    result_str = str(decode("-3000"))
    assert result_str == "instruction:-3000 op_code:30 param:0 name:ADD"
    result_str = str(decode("+1001"))
    assert result_str == "instruction:+1001 op_code:10 param:1 name:READ"
    result_str = str(decode("-1002"))
    assert result_str == "instruction:-1002 op_code:10 param:2 name:READ"
    result_str = str(decode("+1111"))
    assert result_str == "instruction:+1111 op_code:11 param:11 name:WRITE"

    with pytest.raises(Exception):
        decode("+9999")
