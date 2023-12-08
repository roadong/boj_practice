import sys
sys.setrecursionlimit(10 ** 6)

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N = int(input())

tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y = map(int, input().split())
    # [이 노드를 중심 으로][연결 되어 있는 자식 노드]
    tree[x].append(y)
    tree[y].append(x)

visited = [False for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]


def find_min_early_adapter(idx):

    visited[idx] = True
    dp[idx][0], dp[idx][1] = 0, 1

    for i in tree[idx]:
        i: int
        if not visited[i]:
            find_min_early_adapter(i)
            dp[idx][0] += dp[i][1]
            dp[idx][1] += min(dp[i][0], dp[i][1])


find_min_early_adapter(1)
print(min(dp[1][0], dp[1][1]))




