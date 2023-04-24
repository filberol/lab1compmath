from commands.command import Command


class Show(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        print(self.state_manager.get_matrix())
