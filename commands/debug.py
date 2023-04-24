from commands.command import Command


class DebugSwitch(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute_command(self, arguments):
        self.state_manager.switch_debug()
        if self.state_manager.is_debugging():
            print("Debug on")
        else:
            print("Debug off")
