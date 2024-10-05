N, M = map(int, input().split())

A = [int(input()) for _ in range(N)]
A.sort()

i = 0
j = 1
minDiff = 2000000000

while j < N:
    diff = A[j] - A[i]

    if diff >= M:
        minDiff = min(minDiff, diff)
        i += 1
    else:
        j += 1

    # i가 j와 같아지면 j도 증가
    if i == j:
        j += 1

print(minDiff)
