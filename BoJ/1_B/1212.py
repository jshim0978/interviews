# 11001100  314


import math

if __name__ == '__main__':

    # N, B = map(int, input().split())
    n = input()

    if n == '0':
        print('0')
    else:
        s = '' + bin(int(n, 8))
        print(s.lstrip("0b"))


