if __name__ == '__main__':
    n = int(input())

    temp = []
    temp.append(1)
    ten = 10

    for i in range(1, 3000):
        temp.append(temp[i-1] * ten // (i))
        ten += 1

    print(temp[n] % 10007)