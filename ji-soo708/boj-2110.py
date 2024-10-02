# boj-2110: 공유기 설치
# 집 n개가 있는데 공유기 c개를 설치
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하기
import sys

input = sys.stdin.readline
n,c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])
ans = 0

def search(house, s, e):
    global ans
    if s>e: return
    mid = (s+e)//2
    # 최근 공유기 설치 위치
    cur_h = house[0]
    cnt = 1

    for i in range(1, n):
        if house[i]-cur_h>=mid:
            cnt += 1
            cur_h = house[i]
    
    # 공유기가 생각보다 많이 설치되면
    if cnt>=c:
        ans = mid
        s = mid+1
    else:
        e = mid-1

    search(house, s, e)

search(house, 1, house[-1])
print(ans)
