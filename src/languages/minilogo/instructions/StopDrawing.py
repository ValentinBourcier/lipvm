class StopDrawing:

    def __str__(self):
        return 'StopDrawing'

    def execute(self, stack, global_variables, heap):
        global_variables['drawing'] = False