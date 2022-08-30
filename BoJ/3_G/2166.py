import sys

N = int(sys.stdin.readline())

arr = []

for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    arr.append((X, Y))

# print(arr)
arr.append(arr[0])

up = 0
down = 0

for i in range(len(arr) - 1):
    up += (arr[i][0] * arr[i + 1][1])
    down += (arr[i][1] * arr[i + 1][0])

if up-down < 0:
    ans = (down - up) / 2
else:
    ans = (up - down) / 2
    
print(ans)
