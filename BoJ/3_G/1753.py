# find the shortest path for given directional graph
# input : on the first line, 2 integers V, E (1<=V<=20,000, 1<=E<=300,000)
#         on the second line, 1 integer K (1<=K<=V)
#         on the next E lines, 3 integers u, v, w (1<=u, v<=V, 1<=w<=10)
#         u, v : starting point, ending point
#         w : weight of the edge
# output : print the shortest path from K to every vertex
#          if there is no path, print "INF"

import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

INF = 1e9
distance = [INF] * (V + 1)
distance[K] = 0
queue = []
heapq.heappush(queue, (0, K))

while queue:
    dist, now = heapq.heappop(queue)
    if distance[now] < dist:
        continue
    for v, w in graph[now]:
        cost = dist + w
        if cost < distance[v]:
            distance[v] = cost
            heapq.heappush(queue, (cost, v))

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

