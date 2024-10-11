# boj-14502: 연구소
# 연구소에 벽 3개만 세워서 최대의 안전 영역의 구하자
import sys
from collections import deque
import copy

input = sys.stdin.readline
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dy,dx = [-1,1,0,0],[0,0,-1,1]
def bfs():
    global ans
    t_board = copy.deepcopy(board)
    q = deque()
    for i in range(n):
        for j in range(m):
            if t_board[i][j]==2:
                q.append((i,j))
    while q:
        cy,cx = q.popleft()
        for d in range(4):
            ny,nx = cy+dy[d], cx+dx[d]
            if 0<=ny<n and 0<=nx<m and t_board[ny][nx]==0:
                t_board[ny][nx]=2
                q.append((ny,nx)) 

    cnt = 0
    for i in t_board:
        cnt += i.count(0)
    ans = max(ans, cnt)
    
def backtracking(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                board[i][j]=1
                backtracking(cnt+1)
                board[i][j]=0
backtracking(0)       
print(ans)
