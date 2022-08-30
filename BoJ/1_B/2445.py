if __name__ == '__main__':
    n = int(input())

    if n == 1:
        print('**')
    else:
        for i in range(n-1):
            print('*'*(i+1) + ' '*(2*n-2*i-2 ) + '*'*(i+1))

        print('*' * (2*n))

        for i in range(n-1):
            print('*'*(n-i-1) + ' '*(2*i +2) + '*'*(n-i-1))
