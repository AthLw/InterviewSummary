import sys

def add_time(start, duration):
    temp = start.split(':')
    mins = int(temp[1])+int(duration)
    newmins = mins%60
    if newmins < 10:
        newmins = '0'+str(newmins)
    else:
        newmins = str(newmins)
    addition = mins//60
    hour = int(temp[0])+addition
    if hour < 10:
        hour = '0'+str(hour)
    else:
        hour = str(hour)
    return hour+':'+newmins

M = int(sys.stdin.readline().strip())
for _ in range(M):
    N = int(sys.stdin.readline().strip())
    max_users = 0
    events = []
    for i in range(N):
        temp = sys.stdin.readline().strip().split()
        events.append((temp[0], 0, int(temp[1])))
        endtime = add_time(temp[0], temp[2])
        events.append((endtime, 1, int(temp[1])))
    events.sort(key=lambda x: x[0])
    now_users = 0
    for e in events:
        if e[1]:
            now_users -= e[2]
        else:
            now_users += e[2]
        # print("now: {}, users: {}, event: {}".format(e[0], now_users, e[1]))
        if now_users > max_users:
            max_users = now_users
    print(max_users)