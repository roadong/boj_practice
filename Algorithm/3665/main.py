import sys
from collections import deque

input_line = sys.stdin.readline

Q = int(input_line())

# 3
# 5
# 5 4 3 2 1
# 2
# 2 4
# 3 4
# 3
# 2 3 1
# 0
# 4
# 1 2 3 4
# 3
# 1 2
# 3 4
# 2 3

for _ in range(Q):
    N = int(input_line())
    degree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    prize_list = list(map(int, input_line().split()))
    result = []
    d_queue = deque()
    for i in range(N - 1):
        for child in range(i + 1, N):
            graph[prize_list[i]].append(prize_list[child])
            degree[prize_list[child]] += 1

    M = int(input_line())
    for _ in range(M):
        a, b = map(int, input_line().split())
        # a와 연결된 간선을 모두 탐색
        # 간선이 이미 연결 되어있다면 관계를 바꿔준다
        if b in graph[a]:
            graph[a].remove(b)
            degree[b] -= 1
            graph[b].append(a)
            degree[a] += 1
        # 탐색 후 간선이 연결 되어있지 않은 관계라면 신규
        else:
            graph[b].remove(a)
            degree[a] -= 1
            graph[a].append(b)
            degree[b] += 1

    # 위상정렬을 위해 진입차수가 0인 것을 큐에 넣어 준다
    for i in range(1, N + 1):
        if degree[i] == 0:
            d_queue.append(i)

    # 위상정렬을 수행하지 못한다면 -> 사이클이 생겼다 (등수를 정할 수 없다)
    if not d_queue:
        print("IMPOSSIBLE")
        continue
    answer = []

    # Topology sort
    while d_queue:
        dedicate_x = d_queue.popleft()
        answer.append(dedicate_x)

        for idx in graph[dedicate_x]:
            idx: int
            degree[idx] -= 1
            if degree[idx] == 0:
                d_queue.append(idx)

    print("IMPOSSIBLE") if len(answer) < N else print(*answer)
