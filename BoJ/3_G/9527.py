import sys
import math

A, B = map(int, sys.stdin.readline().split())


def number_of_ones(num):
    if num == 0:
        return 0
    n = int(num.bit_length()-1)
    return int((2 ** (n - 1)) * n) + number_of_ones(num - (2 ** n)) + num - ((2 ** n) - 1)


print(number_of_ones(B) - number_of_ones(A - 1))
