


# l1 = [3, 4, 2, 1, 3, 3]
# l2 = [4, 3, 5, 3, 9, 3]
#
#
# l1s = [1, 2, 3, 3, 3, 4]
# l2s = [3, 3, 3, 4, 5, 9]


lines = open("input.txt").read().splitlines()
listx, listy = [], []
for line in lines:
    x, y = line.split()
    listx.append(int(x))
    listy.append(int(y))
listx = sorted(listx)
listy = sorted(listy)

diff = list()

def reconcile(list1, list2):
    if len(list1) != len(list2):
        exit(1)

    diffsum = 0
    for i in range(len(list1)):
        print(list1[i])
        d = abs(list1[i] - list2[i])
        diff.append(d)
        diffsum = diffsum + d
    #print(diff)
    print(diffsum)


reconcile(listx, listy)
