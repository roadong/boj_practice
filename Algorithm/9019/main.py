import sys
from collections import deque

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    visited = [False for _ in range(10001)]
    deq = deque()
    deq.append([a, ''])
    visited[a] = True

    while deq:
        num, command = deq.popleft()

        if num == b:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            deq.append([d, command + 'D'])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            deq.append([s, command + 'S'])

        l = num // 1000 + (num % 1000) * 10
        if not visited[l]:
            visited[l] = True
            deq.append([l, command + 'L'])

        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            deq.append([r, command + 'R'])
