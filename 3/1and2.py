
from aocd import get_data
import re

d = get_data(day=3, year=2024)
td1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

td2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"




def part1(data):
    total = 0
    for ii in data:
        total += int(ii[0]) * int(ii[1])
    print(total)

def part2(data):
    total = 0
    enabled = True
    for ii in data:
        if ii[0] == "don't()":
            enabled = False
        elif ii[0] == "do()":
            enabled = True

        if enabled and ii[1] != "":
            total += int(ii[1]) * int(ii[2])
    print(total)

res1 = re.findall(r"mul\((\d+),(\d+)\)", d)
part1(res1)

res2 = re.findall(r"(don't\(\)|do\(\))|mul\((\d+),(\d+)\)", d)
part2(res2)
