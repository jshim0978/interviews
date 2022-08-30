# 1676, 2004, 6588  todo~
import math

if __name__ == '__main__':

    number = int(input())
    temp = str(math.factorial(number))
    count = 0

    for i in range(len(temp)):
        if temp[-1] == '0':
            count += 1
            temp = temp[:len(temp)-1]
        else:
            print(count)
            break