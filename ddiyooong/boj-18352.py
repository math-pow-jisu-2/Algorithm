import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0

queue = deque([X])

while queue:
    current = queue.popleft()

    for neighbor in graph[current]:
        if distance[neighbor] == -1: # 방문확인
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

result = [i for i in range(1, N + 1) if distance[i] == K]

if result:
    for city in result:
        print(city)
else:
    print(-1)
