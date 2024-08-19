import sys

n = int(sys.stdin.readline().strip())
pwd = sys.stdin.readline().strip()
pwd_len = len(pwd)
all_input = set()
all_len = {}
for l in sys.stdin:
    temp = l.strip()
    if temp in all_input:
        continue
    all_input.add(temp)
    if len(temp) not in all_len.keys():
        all_len[len(temp)] = 1
    else:
        all_len[len(temp)] += 1
    

cnt = 0
for k,v in all_len.items():
    if k < pwd_len:
        cnt += v
    elif k > pwd_len:
        continue

print("{} {}".format(cnt+1, cnt+all_len[pwd_len]))