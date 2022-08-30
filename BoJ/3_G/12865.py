import sys

N, K = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N)]
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    arr[i].append(W)
    arr[i].append(V)

# print(arr)
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(K + 1):
        if j < arr[i][0]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i][0]] + arr[i][1])

print(dp[N-1][K])
# print(dp)
