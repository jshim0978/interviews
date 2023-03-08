N = int(input())
ans = 0

for i in range(N):
    temp = 0
    A, B, C = map(int, input().split())

    if A == B == C:
        temp += 10000 + A * 1000
    elif A == B or B == C or C == A:
        if A == B:
            temp +=1000 + A * 100
        else:
            temp +=1000 + C * 100

    else:
        temp +=max(A, B, C) * 100

    if ans < temp:
        ans = temp


print(ans)