if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(' '*(n-i-1) + '*'*(2*i +1))

