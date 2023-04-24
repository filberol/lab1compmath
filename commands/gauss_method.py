from commands.command import Command
from matrix.matrix_solver import gauss_solve
import time


class GaussMethod(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        if self.state_manager.get_matrix().is_empty():
            print("Cannot count empty matrix.")
            return
        start = round(time.time()*1000)
        result = gauss_solve(self.state_manager.get_matrix())
        # Print answers and errors
        try:
            for i in range(result[0].dimension()):
                print(f'x{i + 1} = {result[1][i]:.5f}')
            for i in range(result[0].dimension()):
                print(f"Err in equation {i + 1}: {result[2][i]:.2e}")
        except TypeError:
            pass
        if self.state_manager.is_debugging():
            print("Time elapsed " + str(round(time.time()*1000) - start) + " ms")
