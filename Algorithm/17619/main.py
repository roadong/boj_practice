import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N, Q = map(int, input().split())
parent = []


def init(log_num):
    global parent
    parent = [i for i in range(log_num + 1)]


def find(u):
    if parent[u] == u:
        return u

    parent[u] = find(parent[u])
    return parent[u]


def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

    return True


log = [()]
for i in range(N):
    x1, x2, y = map(int, input().split())
    log.append((x1, x2, y, i+1))

log = sorted(log)


max_log = log[1][1]
init(N)
ni = 0
for i in range(1, len(log) - 1):
    ni = i + 1
    if max_log >= log[ni][0]:
        union(log[i][3], log[ni][3])

    max_log = max(max_log, log[ni][1])


for _ in range(Q):
    x, y = map(int, input().split())
    if find(x) == find(y):
        print('1')
    else:
        print('0')
