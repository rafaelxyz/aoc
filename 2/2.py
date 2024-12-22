
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
lines = open("input.txt").read().splitlines()
lines = [list(map(int, line.split())) for line in lines]
 
def is_safe(nums):
    # gaps = [abs(b-a) for a, b in zip(nums, nums[1:])]
    pnum = None
    safe = True
    for num in nums:
        if pnum:
            diff = abs(num - pnum)
            if diff > 3 or diff == 0:
                safe = False
        pnum = num
    
    if (nums == sorted(nums)) or (nums == sorted(nums,reverse = True)):
        if safe:
            return True
    return False
 
safe = 0
nums = []
for line in lines:
    for i in range (0, len(line)):
        nums = line.copy()
        nums.pop(i)
        if is_safe(nums):
            safe += 1
            break
print(safe)
