from collections import deque

N = int(input())

dq = deque([i for i in range(1, N+1)])

while(len(dq) >1):
    dq.popleft()
    move_num = dq.popleft()
    dq.append(move_num)

print(dq[0])
