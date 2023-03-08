import sys

n, m = map(int, sys.stdin.readline().split())

a = []
for i in range(n):
    a += [list(map(int, sys.stdin.readline().split()))]

b = []
for j in range(n):
    b += [list(map(int, sys.stdin.readline().split()))]


for i in range(n):
    for j in range(m):
        a[i][j] = a[i][j] + b[i][j]

for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()