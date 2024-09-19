# boj-18310: 안테나
# 일직선 마을에 여러 집이 위치함
# 모든 집까지의 거리 총 합이 최소가 되는 특정 위치에 한 개 안테나 설치
import sys

input = sys.stdin.readline
n = int(input())
houses = sorted(list(map(int, input().split())))

print(houses[(n-1)//2])
