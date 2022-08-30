import sys

N = int(sys.stdin.readline())

arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))

big = 100000007

for rgb in range(3):
    dp = [[0 for _ in range(N)] for _ in range(3)]

    for color in range(3):
        if color == rgb:
            dp[color][0] = arr[0][color]
            continue
        dp[color][0] = big

    for i in range(1, N):
        dp[0][i] = arr[i][0] + min(dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = arr[i][1] + min(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] = arr[i][2] + min(dp[0][i - 1], dp[1][i - 1])

    for check in range(3):
        if check == rgb:
            continue
        big = min(big, dp[check][-1])
print(big)
