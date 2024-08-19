import sys

temp = sys.stdin.readline().strip().split()
n,m,k = int(temp[0]), int(temp[1]), int(temp[2])
decrease = []
for _ in range(n):
    temp = sys.stdin.readline().strip().split()
    x,y,w = int(temp[0]), int(temp[1]), int(temp[2])
    decrease.append((x,y,x+w))
weapons = []
for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    e,h = int(temp[0]), int(temp[1])
    weapons.append((e,h))

def comp(x1, x2):
    if x1[0] == x2[0]:
        if x1[1] == x2[1]:
            return x1[2] < x2[2]
        else:
            return x1[1] < x2[1]
    else:
        return x1[0] < x2[0]

decrease.sort(key=lambda x: x[0])
# print(decrease)
def clac_res(w):
    # pos = -1
    # left = 0
    # right = n
    # while left <= right and left >= 0 and right < n:
    #     if decrease[left][0] >= val:
    #         return left
    #     elif decrease[right][0] < val:
    #         return -1
    index = 0
    tempcost = 0
    while index < n:
        if decrease[index][0] > w[0]:
            break
        elif decrease[index][2] >= w[0] and decrease[index][1] < w[1]:
            tempcost += 1
            # print("{} and {} is joint.".format(decrease[index], w))
        index += 1
    return tempcost

costs = 0
for i in weapons:
    costs += clac_res(i)
print(costs)