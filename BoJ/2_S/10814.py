# 정렬 -  10814, 10825, 10989, 11652, 11004

# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

if __name__ == '__main__':
    N = int(input())
    temp = []
    for i in range(N):
        temp.append(list(input().split()))

    temp.sort(key=lambda temp: int(temp[0]))
    for i in range(N):
        print(temp[i][0], temp[i][1])



