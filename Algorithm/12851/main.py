import sys
from collections import deque

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N, K = map(int, input().split())

queue = deque()
queue.append(N)
way = [0] * 100001
cnt, result = 0, 0
while queue:
    p1 = queue.popleft()
    temp = way[p1]
    # found !
    if p1 == K:
        result = temp
        cnt += 1
        continue

    # 움직일 수 있는 방법 (Bfs)
    for i in [p1 - 1, p1 + 1, 2 * p1]:
        # 3가지로 움직일 때 i는 3가지 방법의 위치
        # 허용범위, 현재 위치를 방문한 적이 없거나 현재 위치에 이전 경로가 여러가지인 경우
        if 0 <= i < len(way) and (way[i] == 0 or way[i] == way[p1] + 1):
            # 해당 위치에 이동한 횟수를 추가 한다
            way[i] = way[p1] + 1
            # 현재 이동한 위치를 큐에 넣는다
            queue.append(i)

print(result)
print(cnt)

