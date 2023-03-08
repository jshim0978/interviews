import math

if __name__ == '__main__':
    testCases = int(input())

    for i in range(testCases):
        A, B = map(int, input().split())
        print(A*B // math.gcd(A, B))


    