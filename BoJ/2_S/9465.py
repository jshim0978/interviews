if __name__ == '__main__':
    testCaseNo = int(input())


    for i in range(testCaseNo):
        col = int(input())
        sticker = []
        for j in range(2):
            sticker.append(list(map(int, input().split())))
        sticker[0].append(0)
        sticker[1].append(0)

        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]
        for t in range(2, col):
            sticker[0][t] += max(sticker[1][t-1], sticker[1][t-2])
            sticker[1][t] += max(sticker[0][t-1], sticker[0][t-2])



        maxVal = max(sticker[0][col-1], sticker[1][col-1])




        print(maxVal)
