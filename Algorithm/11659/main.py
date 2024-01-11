import sys

input_line = sys.stdin.readline

N, M = map(int, input_line().split())

q = [0]

# prefix sum
idx = 1
for element in list(map(int, input_line().rstrip().split(' '))):
    if idx == 1:
        q.append(element)
    else:
        q.append(q[idx - 1] + element)

    idx += 1

for _ in range(M):
    start, end = map(int, input_line().split())
    print(q[end] - q[start - 1])