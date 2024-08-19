import sys

temp = sys.stdin.readline().strip().split()
n,m = int(temp[0]),int(temp[1])
records = []
final = [False for _ in range(n)]
not_change_list = set()
suffix = []
lattemp = [False for _ in range(n)]
latfix = []

def deepcopy(l):
    temp = []
    for i in l:
        temp.append(i)
    return temp

def compare(x1, x2):
    return any([x1[i]!=x2[i] for i in range(len(x1))])

def myand(x1, x2):
    return [x1[i] or x2[i] for i in range(len(x1))]

for i in range(m):
    temp = sys.stdin.readline().strip().split()
    l,r = int(temp[0]),int(temp[1])
    records.append((l,r))
    flag = False
    while l <= r:
        if not final[l-1]:
            final[l-1] = True
            flag = True
        l += 1
    suffix.append(deepcopy(final))
    if not flag:
        not_change_list.add(i)

for i in reversed(range(m)):
    flag = False
    l,r = records[i][0],records[i][1]
    while l <= r:
        if not lattemp[l-1]:
            lattemp[l-1] = True
            flag = True
        l += 1
    latfix.insert(0, deepcopy(lattemp))
    if not flag:
        not_change_list.add(i)

res = 0
for i in range(m):
    if i in not_change_list:
        res += 1
    else:
        if i < 1:
            if not compare(latfix[1], final):
                res += 1
        elif i >= n-1:
            if not compare(suffix[n-2], final):
                res += 1
        elif not compare(myand(suffix[i-1], latfix[i+1]), final):
            res += 1
print(res)