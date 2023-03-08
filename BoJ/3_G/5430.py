from collections import deque
import sys

T = int(sys.stdin.readline())

isEmpty = False

for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()[1:-2].split(",")

    if arr[0] != '':
        arr = deque(arr)
    else:
        arr = deque()

    flag = True

    for i in p:
        if i == "R":
            flag = not flag
        elif i == "D":
            if len(arr) == 0:
                print("error")
                isEmpty = True
                break
            if flag:
                arr.popleft()
            else:
                arr.pop()

    if not flag:
        arr.reverse()

    if not isEmpty:
        print("[", end="")
        for i in range(len(arr)):
            print(arr[i], end="")
            if i != len(arr) - 1:
                print(",", end="")
        print("]")
    isEmpty = False
