import re


class virtualMachine:
    def __init__(self):
        self.vmAccumulator = 0
        self.mainMemory = list(range(100))
        self.nextInstruction = None
        self.exit = False
