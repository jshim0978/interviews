# 터렛

import math

if __name__ == '__main__':

    testCase = int(input())

    for i in range(testCase):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        centerDistance = math.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)))

        sameCenter = (x1 == y1) and (x2 == y2)

        sameRadius = r1 == r2

        firstBigger = r1 > r2
        secondBigger = r2 > r1


        #일치
        if centerDistance == 0 and sameRadius:
            print('-1')

        # 만나지 않음
        elif centerDistance > r1 + r2:
            print('0')
        elif centerDistance + r2 < r1 or centerDistance + r1 < r2:
            print('0')

        #외접
        elif centerDistance == r1 + r2:
            print(1)
        #내접
        elif centerDistance + r1 == r2 or centerDistance + r2 == r1:
            print(1)
        #두번 만남
        else :
            print(2)


