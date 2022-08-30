import sys

N, B = map(int, sys.stdin.readline().split())
matrix = [[*map(int, input().split())] for _ in range(N)]


def matrix_multiply(A, B):
    n = len(A)
    C = [[0]*n for j in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += A[i][k] * B[k][j]
            C[i][j] = temp % 1000
    return C


def matrix_pow(A, n):
    if n == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    else:
        temp = matrix_pow(A, n // 2)
        if n % 2:
            return matrix_multiply(matrix_multiply(temp, temp), A)
        else:
            return matrix_multiply(temp, temp)


temp = matrix_pow(matrix, B)

for r in temp:
    print(*r)




