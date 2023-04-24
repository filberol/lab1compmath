from commands.exit import Exit
from commands.show import Show
from commands.read_matrix import ReadMatrix
from commands.load_matrix import LoadMatrix
from commands.pwd import Pwd
from commands.count_determinant import CountDeterminant
from commands.make_triangle import MakeTriangle
from commands.generate_matrix import GenerateMatrix
from commands.debug import DebugSwitch
from commands.backup import MakeBackup
from commands.restore import MakeRestore
from commands.gauss_method import GaussMethod
from state_manager import StateManager


def read_command(command_dict):
    input_line = input("-> ").split(" ")
    command = input_line.pop(0)
    try:
        command_dict[command].execute_command(input_line)
    except KeyError:
        print("Unknown command.")


if __name__ == '__main__':
    manager = StateManager(False)
    commands = {
        "exit": Exit(),
        "pwd": Pwd(),
        "show": Show(manager),
        "read": ReadMatrix(manager),
        "load": LoadMatrix(manager),
        "deter": CountDeterminant(manager),
        "triangle": MakeTriangle(manager),
        "generate": GenerateMatrix(manager),
        "debug": DebugSwitch(manager),
        "backup": MakeBackup(manager),
        "restore": MakeRestore(manager),
        "solve": GaussMethod(manager)
    }
    while True:
        read_command(commands)
