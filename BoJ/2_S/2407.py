import sys
from itertools import combinations

a, b = map(int, sys.stdin.readline().split())

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(a) // factorial(b) // factorial(a - b))

