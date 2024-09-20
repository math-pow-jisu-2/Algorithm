# boj-2606: 바이러스
# 한 컴터가 바이러스 걸리면 연결된 모든 컴터가 감염됨
# 1번 컴터가 걸리면 최종적으로 감염된 컴터 수는?
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
nn = int(input())
tree = [[False]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(nn):
    a,b = map(int, input().split())
    tree[a][b] = True
    tree[b][a] = True

ans = 0
def bfs(num):
    global ans
    q = deque()
    q.append(num)
    visited[num] = True
    while q:
        v = q.popleft()
        for i in range(n+1):
            if not visited[i] and tree[v][i]:
                q.append(i)
                visited[i]=True
                ans+=1

bfs(1)
print(ans)
