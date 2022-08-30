import math

if __name__ == '__main__':
    A, B = map(int, input().split())
    ans = ''

    times = math.gcd(A,B)

    for i in range(times):
        ans += '1'

    print(ans)
