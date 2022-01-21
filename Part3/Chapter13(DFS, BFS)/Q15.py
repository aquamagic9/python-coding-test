from collections import deque
from sys import stdin

def bfs(graph, start):
    global distances
    distances[start] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for adj_v in graph[v]:
            if distances[adj_v] == -1:
                queue.append(adj_v)
                distances[adj_v] = distances[v] + 1



N, M, K, start = map(int, stdin.readline().split())
# index == 0 일때는 사용하지 않기 때문에 N + 1
distances = [-1] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in range(M):
    node, adjacency_node = map(int, stdin.readline().split())
    graph[node].append(adjacency_node)

bfs(graph, start)
s = ''
for i in range(1, len(distances)):
    if distances[i] == K:
        s += (str(i) + '\n')
if s:
    print(s)
else:
    print(-1)