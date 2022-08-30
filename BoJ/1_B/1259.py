while True:
    flag = True
    A = str(input())
    if A == '0':
        break
    length = len(A)

    for i in range((length)//2):
        if A[i] != A[length - i - 1]:
            flag = False
            print('no')
            break

    if flag:
        print('yes')