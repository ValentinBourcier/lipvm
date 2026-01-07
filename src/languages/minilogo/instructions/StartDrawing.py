class StartDrawing:

    def __str__(self):
        return 'StartDrawing'

    def execute(self, stack, global_variables, heap):
        global_variables['drawing'] = True