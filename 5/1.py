
from aocd import get_data

rules = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
""".strip()

updates = """
75,47,61,53,29
97,61,53,29,13 
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip()

d = get_data(day=5, year=2024)

d = d.split("\n\n")

updates = d[1]
updates = [list(map(int, u.split(","))) for u in updates.split("\n")]

def is_correct_order(row):
    print(row)
    prev = []
    for r in row:
        prev.append(r)
        for j, x in enumerate(xrules):
            if r == x:
                for p in prev:
                    if yrules[j] == p:
                        return False
    return True

rules = d[0]
rules = [list(map(int, lst.split("|"))) for lst in rules.split("\n")]

xrules = []
yrules = []
for s in rules:
    xrules.append(s[0])
    yrules.append(s[1])


sum = 0
for u in updates:
    r = is_correct_order(u)
    if r:
        if len(u) > 0:
            sum += u[int(len(u) / 2)]

    print(r)
print(sum)
