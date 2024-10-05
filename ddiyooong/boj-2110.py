def can_place_routers(houses, C, distance):
    count = 1  # 첫 번째 집에 공유기 설치
    last_router = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_router >= distance: #다음집부터 distance 거리 확보하고 설치
            count += 1
            last_router = houses[i]  # 공유기를 현재 집에 설치

        if count >= C:  # C개 모두 설치가능해야 true
            return True

    return False


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

l = 1  # 최소 거리
r = houses[-1] - houses[0]  # 최대 거리
result = 0

while l <= r:
    mid = (l + r) // 2

    if can_place_routers(houses, C, mid):
        result = mid  # 최소 거리가 mid일 때 가능한 경우, 더 큰 거리를 시도
        l = mid + 1
    else:
        r = mid - 1  # 최소 거리가 mid일 때 불가능한 경우, 더 작은 거리를 시도

# 결과 출력
print(result)
