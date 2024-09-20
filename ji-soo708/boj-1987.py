# boj-1987: 알파벳
# 상하좌우 이동, 같은 알파벳 적힌 칸으로는 지날 수 없음
# 최대한 몇 칸 지날 수 있는지
import sys

input = sys.stdin.readline
r,c = map(int, input().split())
keyboard = [list(input().rstrip()) for _ in range(r)]
dy,dx = [-1,1,0,0],[0,0,-1,1]
key = [keyboard[0][0]]
ans = 0

def dfs(y,x,cnt):
    global ans
    ans = max(ans, cnt)
    for d in range(4):
        ny,nx = y+dy[d],x+dx[d]
        if 0<=ny<r and 0<=nx<c and not keyboard[ny][nx] in key:
            key.append(keyboard[ny][nx])
            dfs(ny,nx,cnt+1)
            key.remove(keyboard[ny][nx])

dfs(0,0,1)
print(ans)
