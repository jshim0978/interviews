import math

if __name__ == '__main__':
    A, B = map(int, input().split())

    print(math.gcd(A, B))
    print(A*B // math.gcd(A,B))
