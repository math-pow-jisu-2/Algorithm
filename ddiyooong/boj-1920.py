N = int(input())
A = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

A.sort()

for i in targets:
    l, r = 0, N - 1
    isExist = False

    while l <= r:
        mid = (l + r) // 2
        if i == A[mid]:
            isExist = True
            print(1)
            break
        elif i > A[mid]:
            l = mid + 1
        else:
            r = mid - 1

    if not isExist:
        print(0)
