# boj-2839: 설탕 배달
# 정확히 n키로 배달해야 한다면, 최소 봉지 몇 개 가져가면 됨?
# 봉지는 3, 5 키로가 있음
import sys

input = sys.stdin.readline
n = int(input())
dp = [5001]*(n+1)

if n>=3:
    dp[3] = 1
if n>=5:
    dp[5] = 1
for i in range(6, n+1):
    dp[i] = min(dp[i-3], dp[i-5])+1

if dp[n]>=5001:
    print(-1)
else:
    print(dp[n])
