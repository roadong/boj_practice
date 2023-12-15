import sys
sys.setrecursionlimit(200000)

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N, Q = map(int, input().split())
parent = [i for i in range(N + 1)]
edges = []
answer = [False for _ in range(Q)]


def find(x):
    if parent[x] == x:
        return parent[x]
    x = find(parent[x])
    return parent[x]


# 2의 부모 정점은 1 (i의 부모 정점은 i-1)
parent_arr = [0 for _ in range(N + 1)]
# 1번 노드의 부모는 자기자신
parent_arr[1] = 1
for i in range(2, N + 1):
    a = int(input())
    parent_arr[i] = a


for i in range(N - 1 + Q):
    edges.append(list(map(int, input().split())))


cnt = 0
# offline algorithm
# 입력한 데이터를 다 가지고 있는 상황에서 풀이하는 과정
# 입력한 순 풀이(정점이 다 연결되어 있는 상황 -> 경로확인 -> 에지제거 -> 노드 전부 엣지 제거)
# 입력을 다 받고 역순으로 해결 ( 연결이 되어있지 않는 정점 -> 연결 -> 경로확인 -> 노드 전부 연결)
for edge in edges[::-1]:
    edge: list
    if len(edge) == 2:
        # 끊어진 정점의 부모 노드를 찾아 연결
        parent[edge[1]] = parent_arr[parent[edge[1]]]
    else:
        answer[cnt] = find(edge[1]) == find(edge[2])
        cnt += 1

# 역순으로 문제를 풀었기 때문에 정답 역순 나열
for _ in range(Q):
    result = answer.pop()
    if result:
        print("YES")
    else:
        print("NO")

