# 프로그래머스 - 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    answer = -1
    if sum(food_times)<=k: return -1
    
    n = len(food_times)
    q = []
    for i in range(n):
        # 필요 시간, 인덱스
        heapq.heappush(q, (food_times[i], i+1))
    
    pre_t = 0
    while q:
        need_time = (q[0][0]-pre_t)*n
        # 현재 음식 다 먹을 수 있는 경우 후보군에서 제거
        if k>=need_time:
            k-=need_time
            pre_t, pre_num = heapq.heappop(q)
            n -= 1
        else:
            idx = k%n
            q.sort(key=lambda x:x[1])
            answer = q[idx][1]
            break
        
    return answer
