import sys

temp = sys.stdin.readline().strip().split()
n,m = int(temp[0]),int(temp[1])

mincost = 200000
i = 0
while i < n//300:
    j = 30*i
    if m < j:
        j = m
    cost = 30*i
    if n > (300*i + j*90):
        cost += (n- (300*i + j*90))//10
    if cost < mincost:
        mincost = cost
        # print("min cost update: {}, {}, {}, {}".format(i,j,cost,(n- (300*i + j*90))//10))
    i += 1
print(mincost)