
class accumulator:
    def __init__(self):
        self.value = 0
class nextInstruction:
    def __init__(self):
        self.location = 0
class virtualMachine:
    def __init__(self, acc):
        self.vmAccumulator = acc
        self.mainMemory = list(range(100))
        self.nextInstruction = None
        self.exit = False
    


