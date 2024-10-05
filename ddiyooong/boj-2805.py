N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

l = 0
r = trees[-1]
result = 0

while l <= r:
    mid = (l + r) // 2
    total = 0

    # 절단된 목재의 길이 계산
    for tree in trees:
        if tree > mid:
            total += tree - mid
        # 토탈이 M을 초과하면 브레이크
        if total >= M:
            break

    if total >= M:
        result = mid  # total이 M 이상이면 결과 업데이트
        l = mid + 1
    else:
        r = mid - 1  # 부족하면 r을 조정

print(result)
