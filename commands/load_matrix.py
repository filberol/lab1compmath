from commands.command import Command
from matrix.matrix_reader import load_from_file


class LoadMatrix(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        if not arguments:
            print("Not enough arguments!")
        else:
            try:
                matrix = load_from_file(arguments[0])
                if matrix is not None:
                    self.state_manager.set_matrix(matrix)
                    print("Matrix loaded")
                else:
                    print("Error loading matrix!")
            except ValueError:
                print("Wrong values. Try again.")
