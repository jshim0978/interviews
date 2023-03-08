n = int(input())

arr = list(map(int, input().split()))
arr.append(0)
arr.append(0)

cnt_3 = 0
cnt_5 = 0
cnt_7 = 0

for i in range(n):
    if arr[i + 1] > arr[i + 2]:
        leftover = min(arr[i], arr[i + 1] - arr[i + 2])
        cnt_5 += leftover
        arr[i] -= leftover
        arr[i + 1] -= leftover

        most_7 = min(arr[i], min(arr[i + 1], arr[i + 2]))
        cnt_7 += most_7
        arr[i] -= most_7
        arr[i + 1] -= most_7
        arr[i + 2] -= most_7

    else:
        most_7 = min(arr[i], min(arr[i + 1], arr[i + 2]))
        cnt_7 += most_7
        arr[i] -= most_7
        arr[i + 1] -= most_7
        arr[i + 2] -= most_7

        leftover = min(arr[i], arr[i + 1])
        cnt_5 += leftover
        arr[i] -= leftover
        arr[i + 1] -= leftover

    cnt_3 += arr[i]

print(cnt_3 * 3 + cnt_5 * 5 + cnt_7 * 7)
