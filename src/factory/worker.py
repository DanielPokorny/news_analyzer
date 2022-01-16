"""
Třídy pro tvorbu workerů ve factory
"""
import threading

class Worker:
    """
    BaseClass pro workery ve factory
    """
    name = ""
    input_pipe = None
    output_pipe = None
    work = True
    def __init__(self, name, input_pipe, output_pipe):
        """
        name        : jméno workeru
        input_pipe  : trubka, ze které bere vstupy
        output_pipe : trubka, do které zapisuje výstupy
        """
        self.name = name
        self.input_pipe = input_pipe
        self.output_pipe = output_pipe

    def run(self):
        """
        Provádí činnost, dokud work = True
        """
        while self.work:
            self.__do_it__()

    def __do_it__(self):
        pass