from commands.command import Command
from matrix.matrix_solver import gauss_triangle_extended
import time


class MakeTriangle(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        if self.state_manager.get_matrix().is_empty():
            print("Cannot count empty matrix.")
            return
        start = round(time.time()*1000)
        result = gauss_triangle_extended(self.state_manager.get_matrix())
        if self.state_manager.is_debugging():
            print("Time elapsed " + str(round(time.time()*1000) - start) + " ms")
        print("Matrix triangle.")
