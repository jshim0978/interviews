import sys
import collections

N, M = map(int, sys.stdin.readline().split())

full = []
ans = []

for _ in range(N + M):
    line = sys.stdin.readline()
    full.append(line)

ans = [item for item, count in collections.Counter(full).items() if count > 1]
ans.sort()

print(len(ans))
for item in ans:
    print(item.strip('\n'))
