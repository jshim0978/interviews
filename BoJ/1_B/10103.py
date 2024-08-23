import sys

n = int(input())

a, d = 100, 100

for _ in range(n):
    a_roll, d_roll = list(map(int, sys.stdin.readline().split()))
    if a_roll > d_roll:
        d -= a_roll
    elif a_roll < d_roll:
        a -= d_roll

print(a)
print(d)

