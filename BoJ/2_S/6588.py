import sys

arr = [True for _ in range(1000001)]

for i in range(2, 1001):
    if arr[i]:
        for j in range(i + i, len(arr), i):
            arr[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        exit()

    for i in range(2, len(arr)):
        if arr[i] and arr[n - i]:
            print(str(n) + " = " + str(i) + " + " + str(n - i))
            break
