
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


xmas = "XMAS"
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


def find_xmas(txt):
    if type(txt) is str():
        strs = "".join(str(txt)).replace(" ", "")
    else:
        strs = "".join(txt).replace(" ", "")
    # print("xjoint:", strs, end="")
    res1 = re.findall(xmas, strs)
    res2 = re.findall(samx, strs)
    # print(" - ", res1, res2)
    return(len(res1 + res2))


def count_xmas_horizontal_vertical(data):
    total = 0
    for i in range(len(data)):
        xres = find_xmas(data[i, :])
        yres = find_xmas(data[:, i])
        total += xres
        total += yres
    # print("xtotal:", total)
    return total

def count_xmas_diagonal(data):
    total = 0
    for dat in data:
        # print(dat)
        res = find_xmas(dat)
        total += res
    # print("dtotal:", total)
    return total


def get_diagonals(matrix: NDArray) -> list[NDArray]:
    rows, cols = matrix.shape
    diagonals = []
    dd = []
    for i in range(-rows + 1, cols):
        print(i, end="")
        diagonals.append(matrix.diagonal(i))
        print(" diagonal:", matrix.diagonal(i))
    print(" end")
    return diagonals


td1 = np.array(create_matrix(d))
td2 = np.fromfunction(f, (10, 10), dtype=int)
data = td1

print(".")
print_matrix(data)
total = 0
total += count_xmas_horizontal_vertical(data)

diagonals = get_diagonals(data)
print(diagonals)
total += count_xmas_diagonal(diagonals)

diagonals = get_diagonals(np.fliplr(data))
total += count_xmas_diagonal(diagonals)

print("total: ", total)
