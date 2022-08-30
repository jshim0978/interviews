# 숫자채우기

from collections import deque

N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]
num = 1
diagonals = [[] for _ in range(N + M - 1)]
temp = []
move = [(0,1), (1,0)]

for x in range(M):
    for y in range(N):
        diagonals[x+y].append(arr[y][x])

for i in range(len(diagonals)):
    if i > 1:
        num += diagonals[i-1][-1] - diagonals[i-2][0]

    for j in range(len(diagonals[i])):
        diagonals[i][j] = num
        num += 1

for i in range(len(diagonals)):
    if i % 2 != 0:
        for j in range(len(diagonals[i])):
            temp.append(diagonals[i][len(diagonals[i])-j-1])
    else:
        for j in range(len(diagonals[i])):
            temp.append(diagonals[i][j])

q = []
q.append([0, 0])
v = [[0 for _ in range(M)] for _ in range(N)]
v[0][0] = 1
idx = 0
while q:
    cur = q.pop(0)
    arr[cur[0]][cur[1]] = temp[idx]
    idx += 1
    for dr, dc in move:
        nr, nc = cur[0]+dr, cur[1]+dc
        if nr<N and nc<M and v[nr][nc]!=1 :
            v[nr][nc] = 1
            q.append([nr, nc])


for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()
