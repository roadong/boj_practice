import sys

input_line = sys.stdin.readline

N, M = map(int, input_line().split())

tree_heights = list(map(int, input_line().split()))

min_height = 0
max_height = max(tree_heights)

result = 0
while min_height <= max_height:
    cut_tree_sum = 0
    cut_height = (min_height + max_height) // 2
    for tree in tree_heights:
        if tree > cut_height:
            cut_tree_sum += tree - cut_height

    # 가져가야 할 나무 높이보다 적을 때 높이를 낮춘다
    if cut_tree_sum < M:
        max_height = cut_height - 1
    # 가져가야 할 나무 높이보다 많을 때는 높이를 올린다
    else:
        result = cut_height
        min_height = cut_height + 1

print(result)
