from commands.command import Command


class MakeBackup(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        self.state_manager.make_backup()
        print("State saved.")
