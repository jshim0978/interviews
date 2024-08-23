import sys

n = int(input())


for _ in range(n):
    y_total, k_total = 0, 0
    for _ in range(9):
        y, k = list(map(int, sys.stdin.readline().split()))

        y_total += y
        k_total += k

    if y_total > k_total:
        print("Yonsei")
    elif y_total == k_total:
        print("Draw")
    else:
        print("Korea")



