# 3
# 4
# 7
# 10
def solve(num):

    temp = []
    temp.append(1)
    temp.append(1)
    temp.append(2)


    for i in range(3, n+3):
        temp.append(temp[i-1] + temp[i-2] + temp[i-3])

    print(temp[num])

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        n = int(input())
        solve(n)
