import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N, target_group_cnt = map(int, input().split())

ball_list = list(map(int, input().split()))
result = []


# 중간 값에서 가능한 그룹 수를 구한다
def search_possible_group_num(mid_value):
    group_sum, groups = 0, 0
    for i in range(len(ball_list)):
        group_sum += ball_list[i]
        if group_sum > mid_value:
            group_sum = ball_list[i]
            groups += 1

    if group_sum > 0:
        groups += 1

    return groups


def cal_groups_cnt(borderline):
    global result
    group_sum, start, group_cnt = 0, 0, 0
    for i in range(len(ball_list)):
        group_sum += ball_list[i]
        if group_sum > borderline:
            group_sum = ball_list[i]
            result.append(len(ball_list[start:i]))
            start = i
            group_cnt += 1

    if group_sum > 0:
        if (target_group_cnt - group_cnt) == len(ball_list[start:]):
            for i in range(len(ball_list[start:])):
                result.append(1)
        else:
            result.append(len(ball_list[start:]))

    # 이렇게 해도 적다면 하나씩 밖에 답이 없다
    if len(result) < target_group_cnt:
        result = [1 for _ in range(len(ball_list))]

    return result


group_result, find_mid_num = 0, sys.maxsize


# 그룹이 하나로 이뤄졌을 때 제일 큰 값 -> left
# 그룹이 리스트 전부를 그룹으로 했을 때 합산 값 -> right
def binary_search(left, right):
    global group_result, find_mid_num
    if left <= right:
        mid_num = (left + right) // 2
        group_result = search_possible_group_num(mid_num)

        if group_result > target_group_cnt:
            left = mid_num + 1
        else:
            right = mid_num - 1
            if mid_num < find_mid_num:
                find_mid_num = mid_num

        return binary_search(left, right)
    else:
        return find_mid_num


binary_search(max(ball_list), int(sum(ball_list)))
print(find_mid_num)
print(*cal_groups_cnt(find_mid_num))
