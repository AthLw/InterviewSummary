import itertools
import sys

T = int(sys.stdin.readline().strip())
for i in range(T):
    temp = sys.stdin.readline().strip().split()
    n,x = int(temp[0]), int(temp[1])
    a = sys.stdin.readline().strip().split()
    a = [int(i) for i in a]
    if n % 2 == 0:
        number = n//2
    else:
        number = n//2+1
    res = 0
    for i in itertools.combinations(a, number):
        if sum(i) >= x:
            res += 1
    print(res)