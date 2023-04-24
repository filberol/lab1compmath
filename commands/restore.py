from commands.command import Command


class MakeRestore(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        self.state_manager.restore_backup()
        print("State restored.")
