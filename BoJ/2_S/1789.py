A = int(input())

X = ((2 * A) ** 0.5) // 1
if X * (X + 1) > (2 * A) :
    X -= 1
    print(int(X))
else:
    print(int(X))