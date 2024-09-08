# boj-1744: 수 묶기
# 길이 n인 수열의 합을 구하려 함
# 수열의 두 수를 묶고 합을 구하는데 묶은 서는 서로 곱한 후에 더함
# 수열의 합이 최대가 되게 하는 프로그램을 작성하라
import sys

input = sys.stdin.readline
n = int(input())
nums = sorted([int(input()) for _ in range(n)])

# 음수와 양수를 분리
m_nums = []
p_nums = []
zeros = 0
ones = 0

for num in nums:
    if num < 0:
        m_nums.append(num)
    elif num > 1:
        p_nums.append(num)
    # 1은 곱하는 것보다 더하는 게 더 이득
    elif num == 1:
        ones += 1
    # 0은 음수랑 곱해서 최대값 만들어주기
    else:
        zeros += 1

# 음수는 절대값이 큰 순으로 묶음
m_sum = 0
for i in range(0, len(m_nums)-1, 2):
    m_sum += m_nums[i] * m_nums[i+1]
if len(m_nums) % 2 == 1:
    if zeros > 0:
        m_sum += 0
    else:
        m_sum += m_nums[-1]

# 양수는 큰 수부터 묶음
p_nums.sort(reverse=True)
p_sum = 0
for i in range(0, len(p_nums)-1, 2):
    p_sum += p_nums[i] * p_nums[i+1]
if len(p_nums) % 2 == 1:
    p_sum += p_nums[-1]

# 1은 곱하기보다 더하는 게 이득
result = m_sum + p_sum + ones
print(result)
