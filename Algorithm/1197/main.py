import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

V, E = map(int, input().split())

edges = []
for _ in range(E):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))
parent = [i for i in range(V + 1)]
edges.sort()


def find(v1):
    if parent[v1] == v1:
        return parent[v1]
    parent[v1] = find(parent[v1])
    return parent[v1]


def union(v1, v2):
    v1, v2 = find(v1), find(v2)
    if v1 == v2:
        return False

    if v1 < v2:
        parent[v2] = v1
    else:
        parent[v1] = v2

    return True


result = 0
for edge in edges:
    cost, x, y = edge
    if union(x, y):
        result += cost


print(result)
