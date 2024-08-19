import sys

def get_mex(elements):
    mex = []
    tempmex = 0
    tempele = set()
    for i in reversed(range(len(elements))):
        tempele.add(elements[i])
        while tempmex in tempele:
            tempmex += 1
        mex.append(tempmex)
    return reversed(mex)

def calc_min(elements, mex, k, x):
    cost = min(x, k*mex[-1])
    for i in reversed(range(len(elements)-1)):
        cost = min(k*mex[i], x+cost)
    return cost

T = int(sys.stdin.readline().strip())
for _ in range(T):
    temp = sys.stdin.readline().strip().split()
    n,k,x = int(temp[0]), int(temp[1]), int(temp[2])
    temp = sys.stdin.readline().strip().split()
    elements = [int(i) for i in temp]
    mex = get_mex(elements)
    result = calc_min(elements, mex, k, x)
    print(result)