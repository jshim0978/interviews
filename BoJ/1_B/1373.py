# 11001100  314


import math

if __name__ == '__main__':

    # N, B = map(int, input().split())
    n = input()

    if n == '0' :
        print('0')
    else :
        print(oct(int(n, 2)).strip('0o'))
