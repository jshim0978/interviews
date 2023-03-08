import sys

t = int(sys.stdin.readline())

meets = []

for i in range(t):
    start, end = map(int, sys.stdin.readline().split())
    interval = end - start
    meets.append((start, end))


meets.sort(key = lambda x: (x[1], x[0]))

cnt = 1
temp = meets[0][1]
for i in range(1, len(meets)):
    if meets[i][0] >= temp:
        cnt += 1
        temp = meets[i][1]

print(cnt)

