# boj-1920: 수 찾기
import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
target = list(map(int, input().split()))

for t in target:
    start = 0
    end = n-1
    isExist = False
    while start<=end:
        mid = (start+end)//2
        if t == a[mid]:
            print(1)
            isExist = True
            break
        elif t > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if not isExist:
        print(0)
