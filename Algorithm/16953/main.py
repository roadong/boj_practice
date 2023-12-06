import sys
from collections import deque

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

a, b = map(int, input().split())
deq = deque()
deq.append([a, 1])
found = False
while deq:
    num, cnt = deq.popleft()

    if num == b:
        found = True
        print(cnt)
        break
    elif num < b:
        dt = num * 2
        if dt <= b:
            deq.append([dt, cnt+1])
        sft = num * 10 + 1
        if sft <= b:
            deq.append([sft, cnt+1])
    else:
        continue

if not found:
    print(-1)
