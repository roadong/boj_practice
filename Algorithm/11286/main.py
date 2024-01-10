import heapq
import sys

input_line = sys.stdin.readline

N = int(input_line())

# 튜플의 경우 첫번째 원소로 정렬
q = []
for _ in range(N):
    x = int(input_line())

    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            abs_x, x = heapq.heappop(q)
            sub_heapq = [(x, abs_x)]
            while len(q) != 0 and abs_x == q[0][0]:
                abs_n, n = heapq.heappop(q)
                heapq.heappush(sub_heapq, (n, abs_n))

            print(heapq.heappop(sub_heapq)[0])
            for i, j in sub_heapq:
                heapq.heappush(q, (j, i))
    else:
        heapq.heappush(q, (abs(x), x))
