import sys
from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))

l = list(combinations(sorted(arr), 7))

ans = ''
for el in l:
    if sum(el) == 100:
        for eel in el:
            print(eel)

        exit()

