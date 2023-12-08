import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)
# BIT => i까지의 누적 합을 구할 때 이분탐색을 함
# x를 넣을 때 공간을 찾으러 갈때마다 C가 증가

N = int(input())

cnt = 0
M = 1 << 19
binary_index_tree, check, depth = [[0] * (M + 1) for i in range(3)]


# 해당 인덱스까지 합산 -> 해당 값을 삽입 변경과 같다
def bit_sum(i):
    temp = 0
    # 합산은 BIT 인덱스 수의 1
    while i:
        temp += binary_index_tree[i]
        i -= i & -i
    return temp


def update(i):
    check[i] = True
    while i <= M:
        binary_index_tree[i] += 1
        i += i & -i


def find(left, idx, right):
    idx_sum = bit_sum(idx)
    if idx_sum == left and check[idx]:
        return idx
    if idx_sum < left:
        return find(left, idx + (1 << right), right - 1)
    return find(left, idx - (1 << right), right - 1)


for i in range(N):
    x = int(input())
    s = bit_sum(x)
    if binary_index_tree[M] == 0:
        pass
    elif s == 0:
        depth[x] = depth[find(1, M, 18)] + 1
    elif s == binary_index_tree[M]:
        depth[x] = depth[find(s, M, 18)] + 1
    else:
        depth[x] = max(depth[find(s, M, 18)], depth[find(s+1, M, 18)]) + 1

    cnt += depth[x]
    update(x)
    print(cnt)
