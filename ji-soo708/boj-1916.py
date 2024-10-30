# boj-1916: 최소 비용 구하기
# n개 도시, m개 버스
# a에서 b가는데 드는 버스 비용 최소화
import heapq

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int, input().split())
    graph[s].append([e, c])

start, end = map(int, input().split())
distance = [INF]*(n+1)

def dijkstra(start):
    distance[start] = 0 # 시작 노드 거리 0으로
    q = []
    # 시작 노드 거리를 0으로 설정
    heapq.heappush(q, [0, start])
    
    while q:
        # 노드까지의 현재까지의 최소 거리, 노드
        dist, now = heapq.heappop(q)
        if (distance[now]<dist): # 이미 더 짧은 경로 찾음
            continue
        
        for info in graph[now]:
            city, cost = info[0], info[1]
            cost = dist+cost
            
            if distance[city] > cost:
                distance[city] = cost
                heapq.heappush(q, [cost, city])
                
dijkstra(start)
print(distance[end])
