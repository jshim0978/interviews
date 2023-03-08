N = int(input())

arr = [0 for _ in range(N)]

for _ in range(N):
    arr[_] = list(map(int, input().split()))

ans = ''

for i in range(N):
    count = 1
    for j in range(N):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            continue
        elif arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            count += 1
        else:
            continue
    ans += str(count) + ' '

print(ans)