import heapq
import sys

input_line = sys.stdin.readline

N = int(input_line())
q = []
for _ in range(N):
    x = int(input_line())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(-heapq.heappop(q))
    else:
        heapq.heappush(q, -x)
