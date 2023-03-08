import sys
N = int(input())
n_arr = list(map(int, sys.stdin.readline().split()))

M = int(input())
m_arr = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

n_arr.sort()

for i in range(M):
    print(binary_search(n_arr, m_arr[i]))


