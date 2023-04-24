from commands.command import Command
from matrix.matrix_generator import generate_matrix


class GenerateMatrix(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        try:
            dim = int(arguments[0])
            matrix = generate_matrix(dim)
            self.state_manager.set_matrix(matrix)
            print("Generated matrix")
        except (ValueError, IndexError):
            print("Wrong arguments.")
