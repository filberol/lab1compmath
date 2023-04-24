from commands.command import Command
from matrix.matrix_solver import count_determinant
import time


class CountDeterminant(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        if self.state_manager.get_matrix().is_empty():
            print("Cannot count empty matrix.")
            return
        start = round(time.time()*1000)
        det = count_determinant(self.state_manager.get_matrix())
        if self.state_manager.is_debugging():
            print("Time elapsed " + str(round(time.time()*1000) - start) + " ms")
        print(f'Matrix determinant is {det[1]}')
