import sys

input_line = sys.stdin.readline

N = int(input_line())
em_list = list(map(int, input().split()))
tree = [[] for _ in range(N)]
son_cnt = [0 for _ in range(N)]


# 가장 많은 부하직원을 가지고 있는 상사가 가장 오래걸림
# 오래 걸리는 쪽에 먼저 전달해야 최소 전달을 기록 할 수 있다 (시간을 겹치게 되므로)
# 오래 걸리는 상사 탐색 + 정렬
def propagation_info(idx):
    global son_cnt
    # 해당 idx 상사의 하위 직원 수를 담는 트리
    sub_tree = []
    if len(tree[idx]) == 0:
        son_cnt[idx] = 0
    else:
        for sub_e in tree[idx]:
            sub_e: int
            # 해당 부하 직원도 그 밑의 부하 직원 수를 알아야 한다
            propagation_info(sub_e)
            sub_tree.append(son_cnt[sub_e])

        sub_tree.sort(reverse=True)
        son_cnt[idx] = max([sub_tree[i] + i + 1 for i in range(len(sub_tree))])


for i in range(1, N):
    tree[em_list[i]].append(i)

propagation_info(0)
print(son_cnt[0])
