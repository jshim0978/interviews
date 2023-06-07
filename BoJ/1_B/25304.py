tot = int(input())

diff = 0
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    diff += a*b

if diff == tot :

    print('Yes')
else:
    print('No')