#  6588  todo~
import math


def count5(num):
    count = 0
    i = 5
    until = num//i

    while until >= 1:
        count += until
        i *= 5

        until //= 5
    return count


def count2(num):
    count = 0
    i = 2
    until = num//i

    while until >= 1:
        count += until
        i *= 2
        until //= 2

    return count


if __name__ == '__main__':
    N, R = map(int, input().split())
    NR = N-R
    print(min((count5(N) - count5(R) - count5(NR)), (count2(N) - count2(R) - count2(NR))))

