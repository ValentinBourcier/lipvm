class Value:

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return 'Value ' + str(self._value)

    def execute(self, stack, global_variables, heap):
        stack.push(self._value)