import sys

a, b, c = map(int, sys.stdin.readline().split())

# ans = (A ** B) % C
# ans = (A ** B//2) % C * (A ** B//2) % C


def binary_division(A, B, C):
    if B == 0:
        return 1
    if B % 2 == 0:
        return (binary_division(A, B // 2, C) ** 2) % C
    else:
        return (A * binary_division(A, B - 1, C)) % C

print(binary_division(a, b, c))

