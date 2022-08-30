#11653, 10872, 1676, 2004, 6588  todo~
def Prime(n):
    if n & 1 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d = d + 2
    return 0

if __name__ == '__main__':
    numbers = list(map(int, input().split()))

    for num in range(numbers[0], numbers[1]+1):
        if num > 1 and Prime(num) == 0:
            print(num)
        if num == 2:
            print(num)
