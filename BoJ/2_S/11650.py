# 정렬 - 11651, 10814, 10825, 10989, 11652, 11004

# 5
# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3

if __name__ == '__main__':
    N = int(input())
    temp = []
    for i in range(N):
        temp.append(list(map(int,input().split())))

    temp.sort()

    for i in range(N):
        print(str(temp[i][0]) + ' ' + str(temp[i][1]))
