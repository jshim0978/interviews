A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + A * 1000)
elif A == B or B == C or C == A:
    if A == B :
        print(1000 + A * 100)
    else :
        print(1000 + C * 100)

else:
    print(max(A, B, C) * 100)