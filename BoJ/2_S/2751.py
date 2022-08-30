# 정렬 - 2751, 11650, 11651, 10814, 10825, 10989, 11652, 11004

if __name__ == '__main__':
    N = int(input())
    temp=[]
    for i in range(N):
        temp.append(int(input()))
    temp.sort()
    for i in range(N):
        print(temp[i])


