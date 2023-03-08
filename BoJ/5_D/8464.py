arr = [0 for i in range(262145)]


def mobius():
    arr[1] = 1
    for i in range(1, 262144):
        if arr[i] != 0:
            for j in range(2 * i, 262145, i):
                arr[j] -= arr[i]


def find(c):
    ans = c
    for i in range(1, int(c ** 0.5 + 1) // 1):
        ans -= (arr[i] * (c // (i * i)))
    return ans


mobius()
N = int(input())

low = 0
high = 107374182400
while low+1 < high:
    mid = (low + high) // 2

    if find(mid) < N:
        low = mid
    else:
        high = mid


print(int(high))
