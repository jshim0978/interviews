N = int(input())

for i in range(N):
    S, R = input().split()
    P = ''
    S = int(S)
    for j in range(len(R)):
        P += R[j] * S
    print(P)

