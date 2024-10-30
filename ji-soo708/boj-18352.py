# boj-13582: 특정 거리의 도시 찾기
## 1~n까지 도시와 m개의 단방향 도로가 존재.
## x부터 출발해 도달할 수 있는 모든 도시 중 최단 거리가 k인 모든 도시들 번호 출력
### 모든 간선의 비용이 동일 => BFS
### X를 시작점으로 BFS를 수행해 모든 도시까지의 최단거리 계산
### 최단거리가 k이면 해당 도시의 번호를 오름차순으로 출력
import sys
from collections import deque

input = sys.stdin.readline
INF = 1e9
# 도시개수, 도로개수, 거리정보, 출발도시
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
distance = [INF]*(n+1)
distance[x] = 0

def bfs(x):
    q = deque([x])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if distance[next]==INF:
                distance[next]=distance[now]+1
                q.append(next)
bfs(x)
isChecked = False
for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        isChecked = True
if not isChecked:
    print(-1)
