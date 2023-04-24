from commands.command import Command
from matrix.matrix_reader import read_from_input


class ReadMatrix(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        print("Enter matrix below. Dimensions will be detected automatically")
        try:
            matrix = read_from_input()
            self.state_manager.set_matrix(matrix)
            print("Matrix updated.")
        except ValueError:
            print("Wrong values. Try again.")
