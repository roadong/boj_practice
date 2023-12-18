import sys
from heapq import heappush, heappop

input_line = sys.stdin.readline

# N: 아파트 단지 수, K: 통학 정원, S: 학교 좌표
N, K, S = map(int, input().split())

left_route, right_route = [], []

stop_list = []
# 학교를 중심으로 양측의 먼 순서 -> 가까운 순으로 통학시켜야 최소
# 최대힙 이용 (가져올 때 가장먼 곳을 바로 꺼내고, 재방문 다시 먼곳에 넣어야하기 때문)
for _ in range(N):
    p_p, p_n = map(int, input().split())
    # 왼쪽
    if p_p < S:
        # 기본이 최소힙이기 때문에 정렬 기준을 음수로 바꿔준다
        heappush(left_route, (p_p - S, p_n))
    else:
        heappush(right_route, (S - p_p, p_n))

result = 0


def sum_distance(route_list):
    global result
    ride_s_num = 0
    current_ride_sum = 0
    while route_list:
        # 가장 먼 곳 방문
        d, s = heappop(route_list)
        current_ride_sum = max(-d, current_ride_sum)
        # 다태웠을 때 승차초과인 경우
        if s + ride_s_num > K:
            # 거리 중간 정산
            result += current_ride_sum * 2
            # 일단 학교로 가서 다 내리게 한다
            heappush(route_list, (d, s - (K - ride_s_num)))
            ride_s_num, current_ride_sum = 0, 0
        else:
            ride_s_num += s

    if current_ride_sum:
        result += current_ride_sum * 2
        ride_s_num, current_ride_sum = 0, 0


sum_distance(left_route)
sum_distance(right_route)
print(result)
