# boj-18405: 경쟁적 전염
# 바이러스는 빈 칸으로 1초마다 증식
# 번호가 낮은 종류부터 증식
# s초가 지난 후에 (y,x)에 존재하는 바이러스 종류 출력
import sys
from collections import deque

input = sys.stdin.readline
n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s,y,x = map(int, input().split())
dy,dx = [-1,1,0,0],[0,0,-1,1]
virus = []
for i in range(n):
    for j in range(n):
        if board[i][j]: virus.append((board[i][j], i, j, 0))
virus.sort()

q = deque(virus)
while q:
    num, cy, cx, sec = q.popleft()
    if sec==s:
        break
    for d in range(4):
        ny,nx = cy+dy[d], cx+dx[d]
        if 0<=ny<n and 0<=nx<n and board[ny][nx]==0:
            board[ny][nx]=num
            q.append((num, ny, nx, sec+1))

print(board[y-1][x-1])
