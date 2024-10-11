# boj-2230: 수 고르기
# 두 수 골랐을 때 차이가 m이상이면서, 제일 작은 경우 구하기
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])
s,e = 0,0
ans = sys.maxsize

while s<n and e<n:
    if nums[e]-nums[s]>=m:
        ans = min(ans, abs(nums[s]-nums[e]))
        s+=1
    else:
        e+=1

print(ans)
