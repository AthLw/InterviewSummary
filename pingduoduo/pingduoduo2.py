import sys

N = int(sys.stdin.readline().strip())
data = []
finished = []
for _ in range(N):
    temp = sys.stdin.readline().strip().split()
    t,w = int(temp[0]), int(temp[1])
    data.append([t,w])
    finished.append(False)

data.sort(key=lambda x: x[0])
ans = 0
index = 0
queue = []

while not all(finished):
    