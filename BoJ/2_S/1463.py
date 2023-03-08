if __name__ == '__main__':
    n = int(input())
    
    temp = [0 for _ in range(n+1)]


    for i in range(n+1):
        if i == 0 :
            temp[i] = -1
        elif i ==1 :
            temp[i] = 0
        else:
            temp[i] = temp[i-1] + 1

            if i%2 == 0 and temp[i] > (temp[i//2] + 1):
                temp[i] = temp[i//2] + 1

            if i%3 == 0 and temp[i] > (temp[i//3] + 1):
                temp[i] = temp[i//3] + 1

    print(temp[n])



