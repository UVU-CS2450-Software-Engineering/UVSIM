import re


class virtualMachine:
    def __init__(self):
        self.DEFAULT_MEMORY = '+0000'
        self.vmAccumulator = 0
        self.mainMemory = list(range(100))
        self.nextInstruction = 0
        self.exit = False
        self.awaitInput = False
        self.reader = None
