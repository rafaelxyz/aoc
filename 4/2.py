
from aocd import get_data
import re
import numpy as np
from numpy.typing import NDArray


d = get_data(day=4, year=2024)
td1 = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()


xmas = "MAS"
samx = "".join(reversed(xmas))


def f(x, y):
    return 10 * x + y


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value}" for value in row))


def create_matrix(data):
    matrix = list(list())
    i = 0
    for line in data.splitlines():
        larr = list()
        for char in line:
            larr.append(char)
        matrix.append(larr)
        i+=1

    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            pass
    return matrix

data = np.array(create_matrix(d))
td2 = np.fromfunction(f, (10, 10), dtype=int)

print(".")
print_matrix(data)

ahits = []
for i in range(1, len(data)-1):
    for j in range(1, len(data)-1):
        if data[i][j] == "A":
            ahits.append((i, j))

print(ahits)

counter = 0
for i, j in ahits:
    hit = False
    if data[i+1][j+1] == "M" and data[i-1][j-1] == "S" or data[i+1][j+1] == "S" and data[i-1][j-1] == "M":
        hit = True
    if data[i-1][j+1] == "M" and data[i+1][j-1] == "S" or data[i-1][j+1] == "S" and data[i+1][j-1] == "M":
        if hit:
            counter += 1

print(counter)
