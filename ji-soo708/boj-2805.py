# boj-2805: 나무 자르기
# 적어도 m미터 나무 집에 가져가기 위해 절단기에 설정할 수 있는
# 높이의 최댓값은?
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
li = list(map(int, input().split()))

s,e = 1, max(li)
while s<=e:
    mid = (s+e)//2
    temp = 0
    for tree in li:
        if tree>mid:
            temp += (tree-mid)
    
    if temp>=m:
        s = mid+1
    else:
        e = mid-1
print(e)
