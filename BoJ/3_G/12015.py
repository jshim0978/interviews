import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]


def binary_search(num):
    start = 1
    end = len(dp)-1
    while start <= end:
        mid = (start + end) // 2
        if dp[mid] == num:
            return mid
        elif dp[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return start


for element in arr:
    if dp[-1] < element:
        dp.append(element)
    else:
        dp[binary_search(element)] = element

print(len(dp) - 1)
