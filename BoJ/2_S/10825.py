if __name__ == '__main__':
    N = int(input())
    temp = []
    for i in range(N):
        temp.append(list(input().split()))

    temp.sort(key=lambda temp: (-int(temp[1]), int(temp[2]), -int(temp[3]), str(temp[0])))

    for i in range(N):
        print(temp[i][0])