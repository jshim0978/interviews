if __name__ == '__main__':
    n = int(input())
    res = ""

    if not n:
        res += '0'
    else:
        while n != 0:
            if n % (-2):
                res = '1' + res
                n = n // - 2 + 1
            else:
                res = '0' + res
                n //= -2

    print(res)
