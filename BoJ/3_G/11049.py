import sys

N = int(sys.stdin.readline())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    
dp = [[0 for _ in range(N)] for _ in range(N)]

for mid in range(N - 1):
    for i in range(N - 1 - mid):
        j = i + 1 + mid
        dp[i][j] = 1000000007
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1])
            
print(dp[0][N - 1])
