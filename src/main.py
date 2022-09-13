"""
Aplikace pro monitorování RSS kanálů a tvorbu kanálů obahujících zájmové
informace.
tohle smazat
"""
from factory import worker

class A(worker.Worker):
    def __do_it__(self):
        print("a")

if __name__ == "__main__":
    w = worker.Worker(25 ,"b","c")
    a = A("a", "d", "e")
    a.run()
    print(w.input_pipe)
