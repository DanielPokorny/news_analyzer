"""
Třídy pro tvorbu workerů ve factory
"""
class Worker:
    """
    BaseClass pro workery ve factory
    """
    name = None
    input_pipe = None
    output_pipe = None
    def __init__(self, name, input_pipe, output_pipe):
        """
        name        : jméno workeru
        input_pipe  : trubka, ze které bere vstupy
        output_pipe : trubka, do které zapisuje výstupy
        """
        self.name = name
        self.input_pipe = input_pipe
        self.output_pipe = output_pipe
