import sys

N = int(sys.stdin.readline())

num = 0
while N > 0:
    if '666' in str(num):
        N = N - 1
    num += 1

print(num-1)