N = int(input())

arr = []
for i in range(N):
    arr.append(str(input()))



t = list(set(arr))
t.sort(key=str.lower)
t.sort(key=len)

for i in range(len(t)):
    print(t[i])