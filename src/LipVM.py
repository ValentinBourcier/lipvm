import sys

from antlr4 import *

from .languages.minilogo.syntax.LanguageLexer import LanguageLexer
from .languages.minilogo.syntax.LanguageParser import LanguageParser
from .languages.minilogo.Compiler import Compiler

from .Interpreter import Interpreter

from io import StringIO

class LipVM:

    def __init__(self):
        self._compiler = Compiler()
        self._interpreter = Interpreter()

    def load(self, stream):
        lexer = LanguageLexer(stream)
        stream = CommonTokenStream(lexer)
        parser = LanguageParser(stream)
        tree = parser.start()

        if parser.getNumberOfSyntaxErrors() > 0:
            print("syntax errors")
        else:
            self._interpreter.reset()
            self._interpreter.bytecode = self._compiler.compile(tree)

    def load_file(self, path):
        self.load(FileStream(path))
    
    def load_code(self, code):
        self.load(InputStream(code))

    def start(self):
        self._interpreter.start()
    
    def step(self):
        self._interpreter.step()

    def state(self):
        return self._interpreter.state()

if __name__ == '__main__':
    vm = LipVM()
    vm.load_file(sys.argv[1])
    vm.interpreter.start()
    print(vm.interpreter.state())