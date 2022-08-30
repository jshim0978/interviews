import sys

N, M = map(int, sys.stdin.readline().split())

pokedex = []
pokedex_dict = {}

for i in range(N):
    t = sys.stdin.readline().strip()
    pokedex_dict[t] = i + 1
    pokedex.append(t)


for j in range(M):
    query = sys.stdin.readline().strip()
    if query.isnumeric():
        print(pokedex[int(query) - 1])
    else:
        print(pokedex_dict[query])
