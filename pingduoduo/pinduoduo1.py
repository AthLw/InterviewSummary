import sys

def calc_result(data, init_day):
    # if len(data) == 1:
    x = data[0][1]
    d = data[0][2]
    i = 0
    while x+i*d <= init_day:
        i += 1
    return x+i*d
    # else:
    #     i = 0
    #     n = len(data)
    #     visited = [False for _ in range(n)]
    #     visited_days = set()
    #     while not all(visited):
    #         temp = [(j, data[j][1]+data[j][2]*i) for j in range(n)]
    #         for k in temp:
    #             if k[1] > init_day and k[1] not in visited_days:
    #                 visited_days.add(k[1])
    #                 visited[k[0]] = True
    #     return max(visited_days)

N = int(sys.stdin.readline().strip())
all_p = set()
data = {}
for _ in range(N):
    temp = sys.stdin.readline().strip().split()
    p, x, d = int(temp[0]), int(temp[1]), int(temp[2])
    all_p.add(p)
    if p in data.keys():
        data[p].append([p, x, d])
    else:
        data[p] = [[p, x, d]]
last = 0
for _p in sorted(list(all_p)):
    patch = data[_p]
    last = calc_result(patch, last)
print(last)

