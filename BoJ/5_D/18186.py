n, B, C = map(int, input().split())

arr = list(map(int, input().split()))
arr.append(0)
arr.append(0)

cnt_B = 0
cnt_B_C = 0
cnt_B_2C = 0

if B > C:
	for i in range(n):
		if arr[i + 1] > arr[i + 2]:
			leftover = min(arr[i], arr[i + 1] - arr[i + 2])
			cnt_B_C += leftover
			arr[i] -= leftover
			arr[i + 1] -= leftover

			most_7 = min(arr[i], min(arr[i + 1], arr[i + 2]))
			cnt_B_2C += most_7
			arr[i] -= most_7
			arr[i + 1] -= most_7
			arr[i + 2] -= most_7

		else:
			most_7 = min(arr[i], min(arr[i + 1], arr[i + 2]))
			cnt_B_2C += most_7
			arr[i] -= most_7
			arr[i + 1] -= most_7
			arr[i + 2] -= most_7

			leftover = min(arr[i], arr[i + 1])
			cnt_B_C += leftover
			arr[i] -= leftover
			arr[i + 1] -= leftover

		cnt_B += arr[i]

	print(cnt_B * B + cnt_B_C * (B+C) + cnt_B_2C * (B+2*C))

else:
	print(B * sum(arr[:n]))