#1929, 11653, 10872, 1676, 2004, 6588  todo~

if __name__ == '__main__':

    numberOfnumbers = int(input())
    numbers = list(map(int, input().split()))

    res = 0
    for n in range(numberOfnumbers):
        if numbers[n] > 1:
            for i in range(2, numbers[n]):
                if (numbers[n] % i) == 0:
                    break
            else:
                res += 1
    print(res)

