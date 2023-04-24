from commands.command import Command


class Exit(Command):
    def __int__(self, manager):
        Command.__init__(self)

    def execute_command(self, arguments):
        print("Exiting...")
        exit(0)
