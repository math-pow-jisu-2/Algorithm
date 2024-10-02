# boj-1644: 소수의 연속합
# 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있음
# 연속된 소수의 합으로 나타낼 수 있는 경우의 수 구하기
import sys

input = sys.stdin.readline
n = int(input())

def prime_numbers(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]

# 소수 리스트
primes = prime_numbers(n)

s, e = 0, 0
cnt = 0
current_sum = 0

while True:
    if current_sum >= n:
        if current_sum == n:
            cnt += 1
        current_sum -= primes[s]
        s += 1
    elif e == len(primes):
        break
    else:
        current_sum += primes[e]
        e += 1

print(cnt)
