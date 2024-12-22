


l1 = [3, 4, 2, 1, 3, 3]
l2 = [4, 3, 5, 3, 9, 3]
l1s = [1, 2, 3, 3, 3, 4]
l2s = [3, 3, 3, 4, 5, 9]


lines = open("input.txt").read().splitlines()
listx, listy = [], []
for line in lines:
    x, y = line.split()
    listx.append(int(x))
    listy.append(int(y))
listx = sorted(listx)
listy = sorted(listy)


def reconcile(list1, list2):
    if len(list1) != len(list2):
        exit(1)

    score = list()
    for i in list1:
        count = 0
        for j in list2:
            if i == j:
                count = count + 1
        score.append(i * count)

    total = 0
    for s in score:
        total = total + s
    print(total)



#reconcile(l1, l2)
reconcile(listx, listy)
