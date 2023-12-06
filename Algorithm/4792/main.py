import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

parent = []
n, m, k = 0, 0, 0


def init():
    global parent
    parent = [i for i in range(n+1)]


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


def mst(node_count, edge_first, edge_second):
    global parent
    cnt, total_cost = node_count, 0

    for edges, cost in ((edge_first, 0), (edge_second, 1)):
        for u, v in edges:
            if union(u, v):
                total_cost += cost
                cnt -= 1
                if cnt == 1:
                    return total_cost


btree, rtree = [], []

while True:
    n, m, k = map(int, input().split())
    if n == 0:
        break

    btree, rtree = [], []
    for _ in range(m):
        c, f, t = input().split()

        if c == 'B':
            btree.append((int(f), int(t)))
        else:
            rtree.append((int(f), int(t)))

    if len(btree) < k:
        print('0')
        continue
    init()
    min_b = mst(n, rtree, btree)
    init()
    min_r = mst(n, btree, rtree)

    max_b = n - 1 - min_r
    print('1' if min_b <= k <= max_b else '0')
