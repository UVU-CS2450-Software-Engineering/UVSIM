import sys
sys.path.insert(0,'../testt')
# from testt import src
#import ../src
from src import *
#from UVSIM.src import *
def test_vm():
    acc = accumulator()
    obj = virtualMachine(acc)
    assert obj.vmAccumulator.value == 0