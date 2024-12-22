#
# from tokenize import String
#
#
# test_data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""
#
#
# def parse_test_data(data : str):
#     data.strip()
#     return data.split("\n")
#
# def read_file(filename):
#     return open(filename).read().splitlines()
#
# def check_safety(data):
#     i = 0
#     safe_count = 0
#     for row in data:
#         i = i + 1
#         pnum = None
#         safe = True
#         increasing = None
#         for num in row.split(" "):
#             inum = int(num)
#             if pnum:
#                 diff = abs(inum - pnum)
#                 if inum < pnum:
#                     if increasing == True:
#                         safe = False
#                     increasing = False
#                 elif inum > pnum:
#                     if increasing == False:
#                         safe = False
#                     increasing = True
#
#                 if diff > 3:
#                     safe = False
#                 elif diff == 0:
#                     safe = False
#             pnum = inum
#
#
#         if safe:
#             safe_count = safe_count + 1
#     print("safe_count", safe_count)
#
#
#
# data = parse_test_data(test_data)
# #data = read_file("input.txt")
# check_safety(data)
#
import numpy as np

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def parse_test_data(data : str):
    data.strip()
    return data.split("\n")

lines = parse_test_data(test_data)
#lines = open("input.txt").read().splitlines()
data = [list(map(int, line.split())) for line in lines]


def is_safe(line):
    diff = np.diff(line)
    print(diff)
    diff = diff * np.sign(diff[0])
    return int(((diff > 0) & (diff <= 3)).all())


print(sum(is_safe(line) for line in data))
