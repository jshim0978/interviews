N, K = map(int, input().split())

arr = []
count = 0

for i in range(N):
    arr.append(int(input()))

arr.reverse()

for i in range(N):
    if arr[i] > K:

        pass
    else:
        count += K // arr[i]
        K = K - ((K // arr[i]) * arr[i])
        count += K // arr[i]

print(count)