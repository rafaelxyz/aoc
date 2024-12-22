
from aocd import get_data
import re
import numpy as np
from numpy.typing import NDArray


d = get_data(day=5, year=2024)
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

