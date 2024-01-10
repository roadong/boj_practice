import sys
from collections import deque

input_line = sys.stdin.readline

N = int(input_line())
procession = [list(map(int, input_line().rstrip().split(' '))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]


# 해당 노드를 bfs하면 해당 노드에서 방문 가능한 노드들을 다 찾을 수 있다
def bfs(start):
    d_queue = deque([start])
    end_check = [False] * N
    while d_queue:
        x = d_queue.popleft()
        for i in range(N):
            if not end_check[i] and procession[x][i] == 1:
                visited[start][i] = 1
                # 사이클이 생길 수 있어서 탐색한 노드를 제외시켜주자
                end_check[i] = True
                d_queue.append(i)


for idx in range(N):
    bfs(idx)

for row in visited:
    print(*row)
