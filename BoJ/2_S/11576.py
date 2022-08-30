if __name__ == '__main__':
    baseA, baseB = map(int, input().split())
    places = int(input())
    givenNumber = list(map(int, input().split()))
    baseTen = 0
    res = []

    for i in range(places):
        baseTen += givenNumber[places - i - 1] * (baseA ** i)
        givenNumber.pop(places - i - 1)

    while baseTen != 0:
        res.append(str(baseTen % baseB))
        baseTen = baseTen // baseB

    print(' '.join(res[::-1]))
