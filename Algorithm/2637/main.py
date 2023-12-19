import sys
from collections import deque

input_line = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
combine_number = [[0] * (N + 1) for _ in range(N + 1)]
d_queue = deque()
for _ in range(M):
    # X를 만드는데 기본 or 중간 Y 부품 K개가 필요
    X, Y, K = map(int, input_line().split())
    X: int
    Y: int
    K: int
    graph[Y].append((X, K))
    degree[X] += 1

for i in range(1, N + 1):
    if degree[i] == 0:
        d_queue.append(i)

result = []
while d_queue:
    # 진입차수 0 인 것을 꺼낸다
    dedicate_x = d_queue.popleft()

    # 간선 제거
    for idx, weight in graph[dedicate_x]:
        idx: int
        weight: int
        # 해당 부품을 만들기 위한 부품이 없으면 -> 기본 부품
        if sum(combine_number[dedicate_x]) == 0:
            combine_number[idx][dedicate_x] += weight
        # 있다면 -> 중간 부품
        else:
            for j in range(1, N + 1):
                combine_number[idx][j] += combine_number[dedicate_x][j] * weight

        # 간선 제거 -> 진입차수가 0 이면 큐에 삽입
        degree[idx] -= 1
        if degree[idx] == 0:
            d_queue.append(idx)

for x in enumerate(combine_number[N]):
    if x[1] > 0:
        print(*x)

