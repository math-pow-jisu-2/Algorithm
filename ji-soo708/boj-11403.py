# boj-11403: 경로 찾기
# 모든 정점에 대해 i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하기
## 모든 정점에 대해 다 검사해야하므로 플로이드 워셜
import sys

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][k] and board[k][j]:
                board[i][j]=1

for i in range(n):
    print(*board[i])
    