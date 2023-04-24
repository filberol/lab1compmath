from matrix.matrix import Matrix
from matrix.matrix_solver import count_determinant
import random


def generate_matrix(dimensions):
    empty_arr = []
    for row in range(0, dimensions):
        empty_arr.append([0.0] * (dimensions + 1))
    for step in range(0, int(dimensions ** 2)):
        row = random.randrange(0, dimensions, 1)
        col = random.randrange(0, dimensions + 1, 1)
        empty_arr[row][col] = round(random.randrange(-10, 10), 3)
    new_matrix = Matrix(empty_arr)
    while count_determinant(new_matrix)[1] == 0.0:
        row = random.randrange(0, dimensions, 1)
        col = random.randrange(0, dimensions + 1, 1)
        new_matrix.set_element(row, col, round(random.randrange(-10, 10), 3))
    return new_matrix
