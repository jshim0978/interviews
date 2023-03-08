import math

if __name__ == '__main__':

    testCases = int(input())
    for t in range(testCases):
        getNumber = []
        getNumber.append((input().split()))
        temp = []
        sum = 0
        for i in range(int(getNumber[0][0])):
            temp.append(getNumber[0][i+1])

        for j in range(len(temp)):
            for k in range(j+1, len(temp)):
                sum += math.gcd(int(temp[j]), int(temp[j-k]))
        print(sum)


