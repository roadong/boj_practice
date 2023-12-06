import math
import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N, Q = map(int, input().split())
lst = list(map(int, input().split()))

height = math.ceil(math.log2(N))
tree_size = 1 << (height + 1)
stree = [0 for x in range(tree_size)]


def build_stree(stree, node, l, r):
    if l == r:
        stree[node] = lst[l]
        return stree[node]

    mid = l + (r - l) // 2
    stree[node] = build_stree(stree, 2 * node, l, mid) + build_stree(stree, 2 * node + 1, mid + 1, r)
    return stree[node]


def query(s, e, node, l, r):
    if e < l or s > r:
        return 0

    if s <= l and r <= e:
        return stree[node]

    mid = l + (r - l) // 2
    return query(s, e, 2 * node, l, mid) + query(s, e, 2 * node + 1, mid + 1, r)


def update(l, r, node, index, val):
    if index < l or index > r:
        return stree[node]

    if l == r:
        stree[node] = val
        return stree[node]

    mid = l + (r - l) // 2
    stree[node] = update(l, mid, 2 * node, index, val) + update(mid + 1, r, 2 * node + 1, index, val)
    return stree[node]


build_stree(stree, 1, 0, N - 1)

for _ in range(Q):
    s, e, a, b = map(int, input().split())
    print(query(s - 1, e - 1, 1, 0, N - 1)) if s < e else print(query(e - 1, s - 1, 1, 0, N - 1))
    update(0, N - 1, 1, a - 1, b)
