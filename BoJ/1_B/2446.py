if __name__ == '__main__':
    n = int(input())

    if n == 1:
        print('*')
    else:
        for i in range(n):
            print(' '*(i) + '*'*(2*n-1-2*i))



        for i in range(n-1):
            print(' '*(n-i-2) + '*'*(2*i +3))
