"""
Aplikace pro monitorování RSS kanálů a tvorbu kanálů obahujících zájmové
informace.
"""
from factory import worker

if __name__ == "main":
    w = worker.Worker("a","b","c")
    print(w.input_pipe)
