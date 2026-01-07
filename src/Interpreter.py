from .Bytecode import Bytecode
from .Stack import Stack

class Interpreter:

    def __init__(self):
        self.reset()

    def reset(self):
        self._ip = 0
        self._stack = Stack()
        self._globals = {}
        self._heap = {}
        self._bytecode = Bytecode()
        self._interrupt = False

    @property
    def bytecode(self):
        return self._bytecode

    @bytecode.setter
    def bytecode(self, bytecode):
        self._bytecode = bytecode
    
    def ended(self):
        return self._ip >= self._bytecode.size()

    def start(self):
        while not (self._interrupt or self.ended()):
            self.step()
        self._interrupt = False

    def stop(self):
        if self._ip > 0:
            self._interrupt = True

    def step(self):
        self._bytecode.instructions[self._ip].execute(self._stack, self._globals, self._heap)
        self._ip += 1

    def state(self):
        return { 
            'stack': self._stack,
            'globals': self._globals,  
            'heap':  self._heap
        }







