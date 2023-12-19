import sys
from collections import deque

# 7
# 9
# 1 2 4
# 1 3 2
# 1 4 3
# 2 6 3
# 2 7 5
# 3 5 1
# 4 6 4
# 5 6 2
# 6 7 5
# 1 7
# Topology Sort + Critical Path
input_line = sys.stdin.readline

N = int(input_line())
M = int(input_line())

d_queue = deque()
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
spend_time = [0] * (N + 1)

for _ in range(M):
    X, Y, W = map(int, input_line().split())
    X: int
    Y: int
    W: int
    graph[X].append((Y, W))
    reverse_graph[Y].append((X, W))
    degree[Y] += 1

start, end = map(int, input().split())

# 시작지점은 진입차수가 0
# 다른 엣지는 진입차수가 0이 아님
d_queue.append(start)

while d_queue:
    dedicate_x = d_queue.popleft()
    # 큐에 들어가 있는 것은 진입 차수가 0
    # 진입차수가 0인 정점과 이어져있는 정점과의 간선을 모두 찾아 간선을 제거
    for idx, weight in graph[dedicate_x]:
        idx: int  # 연결된 정점
        weight: int  # 이동 시간
        # 다음 도시와 연결된 간선을 제거하면서 걸린시간이 최대인 것을 찾으며 저장
        # 최종적으로 spend_time[시작도시]에 들어가 있는 값은 도착도시까지 걸린 최대 시간
        spend_time[idx] = max(spend_time[idx], spend_time[dedicate_x] + weight)
        # 간선 제거 했으니 진입차수 감소
        degree[idx] -= 1
        if degree[idx] == 0:
            d_queue.append(idx)


print(spend_time[end])


# 역순으로 백트레킹이기 때문에 도착지점은 진입차수가 0이라고 간주
d_queue.append(end)

path_cnt = 0
visited = [False] * (N + 1)
while d_queue:
    dedicate_r_x = d_queue.popleft()

    for idx, weight in reverse_graph[dedicate_r_x]:
        if spend_time[dedicate_r_x] - spend_time[idx] == weight:
            path_cnt += 1
            if not visited[idx]:
                visited[idx] = True
                d_queue.append(idx)

print(path_cnt)
