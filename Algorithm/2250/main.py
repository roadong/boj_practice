import sys

input_line = sys.stdin.readline

# 19
# 1 2 3
# 2 4 5
# 3 6 7
# 4 8 -1
# 5 9 10
# 6 11 12
# 7 13 -1
# 8 -1 -1
# 9 14 15
# 10 -1 -1
# 11 16 -1
# 12 -1 -1
# 13 17 -1
# 14 -1 -1
# 15 18 -1
# 16 -1 -1
# 17 -1 19
# 18 -1 -1
# 19 -1 -1

N = int(input_line())

MAX = sys.maxsize
tree = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
cnt, max_depth = 1, 1
level_cnt = [[MAX, -MAX] for _ in range(N + 1)]

for _ in range(N):
    r, c1, c2 = map(int, input_line().split())
    c1: int
    c2: int
    tree[r] = [c1, c2]
    if c1 != -1:
        degree[c1] += 1
    if c2 != -1:
        degree[c2] += 1


def dfs(check_node, level):

    global cnt, max_depth

    # 노드가 -1이면 없는 노드라 검색 종료
    if check_node == -1:
        return

    max_depth = max(max_depth, level + 1)

    dfs(tree[check_node][0], level + 1)

    level_cnt[level][0] = min(level_cnt[level][0], cnt)
    cnt += 1
    level_cnt[level][1] = max(level_cnt[level][1], cnt)

    dfs(tree[check_node][1], level + 1)


# root가 1인 보장이 없다 -> 진입차수가 0인게 루트
for i in range(1, N + 1):
    if degree[i] == 0:
        dfs(i, 1)
        # 찾으면 끝내버린다
        break

result = [0, 0]
for i in range(1, max_depth):
    if result[1] < level_cnt[i][1] - level_cnt[i][0]:
        result[1] = level_cnt[i][1] - level_cnt[i][0]
        result[0] = i


print(*result)