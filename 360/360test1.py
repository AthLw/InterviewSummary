import sys

n = int(sys.stdin.readline().strip())
order = sys.stdin.readline().strip().split()

result = []
nowhas = set()
day = 1

while day <= n and len(result) < n:
    nowhas.add(int(order[day-1]))
    while len(result)+1 in nowhas:
        result.append(day)
    day += 1

print(result)