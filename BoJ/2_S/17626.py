# every number can be represented in the sum of 4 or less square numbers
# 1. find the number of square numbers that are less than or equal to n
# 2. if n is a square number, return 1
# 3. if n is the sum of two square numbers, return 2
# 4. if n is the sum of three square numbers, return 3
# 5. if n is the sum of four square numbers, return 4
# 6. else, return -1

import sys
import math

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = i
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[n])


