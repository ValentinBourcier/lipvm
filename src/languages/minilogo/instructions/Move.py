class Move:

    def __str__(self):
        return 'Move'

    def execute(self, stack, global_variables, heap):
        position = (stack.pop(), stack.pop())
        if 'drawing' in global_variables and global_variables['drawing'] and 'position' in global_variables:

            line = (global_variables['position'] , position, global_variables['color'])

            if 'lines' in heap:
                heap['lines'].append(line)
            else:
                heap['lines'] = [line]

        global_variables['position'] = position