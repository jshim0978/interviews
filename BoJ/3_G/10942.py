import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1
    else:
        dp[i][i + 1] = 0

for pivot in range(N - 2):
    for i in range(N - 2 - pivot):
        j = i + 2 + pivot
        if arr[i] == arr[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

M = int(sys.stdin.readline())
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print(dp[A - 1][B - 1])
