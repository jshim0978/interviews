import sys

T = int(sys.stdin.readline())

dp = [1] * 1000001

for i in range(2, len(dp)):
    j = 1
    while i * j <= len(dp) - 1:
        dp[i * j] += i
        j += 1

save_sum = [0] * 1000001
for _ in range(1, len(dp)):
    save_sum[_] = save_sum[_-1] + dp[_]

for _ in range(T):
    N = int(sys.stdin.readline())
    # print(sum(dp[1: N + 1]))
    print(save_sum[N])
