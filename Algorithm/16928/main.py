import sys
from collections import deque
from sys import stdin

input_line = stdin.readline

# N: 사다리, M: 뱀
N, M = map(int, input_line().rstrip().split())
jump_map = [[] for _ in range(101)]
visited = [(False, sys.maxsize) for _ in range(101)]


# 사다리는 가까워진다
for _ in range(N):
    # x칸에 도착하면 y번 칸으로 이동
    x, y = map(int, input_line().rstrip().split())
    jump_map[x].append(y)


# 뱀은 멀어진다
for _ in range(M):
    # u칸에 도착하면 v번 칸으로 이동
    u, v = map(int, input_line().rstrip().split())
    jump_map[u].append(v)


# 1부터 방문 -> 해당 방문 위치에서 최소값으로 갱신
def bfs(start):
    d_queue = deque([start])
    visited[start] = (True, 0)

    while d_queue:
        prev_node = d_queue.popleft()

        for dice_num in range(1, 7):
            next_node = prev_node + dice_num
            if 1 < next_node <= 100 and not visited[next_node][0]:
                visited[next_node] = (True, min(visited[prev_node][1] + 1, visited[next_node][1]))
                if len(jump_map[next_node]) != 0:
                    visited[jump_map[next_node][0]] = (True, min(visited[next_node][1],
                                                                 visited[jump_map[next_node][0]][1]))
                    d_queue.append(jump_map[next_node][0])
                else:
                    d_queue.append(next_node)


bfs(1)
print(visited[100][1])
