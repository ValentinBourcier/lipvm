class Color:

    def __str__(self):
        return 'Color'

    def execute(self, stack, global_variables, heap):
        global_variables['color'] = stack.pop()