# boj-18428: 감시 피하기
# 상하좌우 감시 가능
# 장애물 뒤에 숨은 학생들은 볼 수 없음
# 3개 장애물 설치해서 모든 학생들이 감시 피할수 있는지 여부 출력
import sys

input = sys.stdin.readline
n = int(input())
board = [list(input().split()) for _ in range(n)]
teacher, room = [],[]
for i in range(n):
    for j in range(n):
        if board[i][j]=="T":
            teacher.append((i,j))
        elif board[i][j]=="X":
            room.append((i,j))

dy,dx = [-1,1,0,0],[0,0,-1,1]
def search():
    for y,x in teacher:
        for d in range(4):
            for i in range(1, n):
                ny,nx = y+dy[d]*i, x+dx[d]*i
                if 0>ny or 0>nx or ny>=n or nx>=n or board[ny][nx]=="O":
                    break
                elif board[ny][nx]=="S":
                    return False
    return True

def backtracking(depth, idx):
    if depth==3:
        if search():
            print("YES")
            exit()
        return
    
    for i in range(idx, len(room)):
        y,x = room[i]
        board[y][x]="O"
        backtracking(depth+1, i+1)
        board[y][x]="X"

backtracking(0,0)
print("NO")
