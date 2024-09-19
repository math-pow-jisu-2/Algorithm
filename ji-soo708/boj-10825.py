# boj-10825: 국영수
# 1. 국어 점수 감소하는 순서로
# 2. 영어 점수 증가하는 순서로
# 3. 수학 점수 감소하는 순서로
# 4. 이름 사전 순으로 증가하는 순서로 (아스키 기준)
import sys

input = sys.stdin.readline
n = int(input())
li = [input().split() for _ in range(n)]
li.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in li:
    print(i[0])
