import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

sum = 0

for i in range(N):
    for j in range(i+1):
        sum += arr[j]

print(sum)