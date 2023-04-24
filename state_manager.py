import copy
from matrix.matrix import Matrix


class StateManager:
    def __init__(self, debug):
        self.__backup = None
        self.__matrix = Matrix()
        self.__debug = debug

    def get_matrix(self):
        return self.__matrix

    def set_matrix(self, matrix):
        self.__matrix = matrix

    def is_debugging(self):
        return self.__debug

    def switch_debug(self):
        self.__debug = not self.__debug

    def make_backup(self):
        self.__backup = copy.deepcopy(self.__matrix)

    def restore_backup(self):
        self.__matrix = self.__backup
