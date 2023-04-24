from matrix.matrix import Matrix


def map_string_array(array_line):
    return list(map(lambda x: float(x), array_line.split(" ")))


def read_from_input():
    matrix_array = []
    first_line = map_string_array(input())
    matrix_array.append(first_line)
    for i in range(0, len(first_line) - 2):
        matrix_array.append(map_string_array(input()))
    return Matrix(matrix_array)


def load_from_file(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("File does not exist.")
        return None
    matrix_array = []
    first_line = map_string_array(file.readline())
    matrix_array.append(first_line)
    for i in range(0, len(first_line) - 2):
        matrix_array.append(map_string_array(file.readline()))
    return Matrix(matrix_array)
