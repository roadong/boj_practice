import heapq
import sys

input_line = sys.stdin.readline

N = int(input_line())

# 최소힙만 지원
# 최대힙을 사용하려면 -음수로 집어 넣어야 함
min_heap = []
commands = [int(input_line()) for _ in range(N)]

for command in commands:
    if command == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, command)
