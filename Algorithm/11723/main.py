import sys

input_line = sys.stdin.readline

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

# 이게 왜 안될까? 🤔
M = int(input_line())
S = set()


def toggle(x):
    global S
    if x in S:
        S.discard(x)
    else:
        S.add(x)


def set_all():
    return set([i for i in range(1, 21)])


def set_empty():
    return set()


def check_set(x):
    global S
    print(1 if x in S else 0)


def set_add(x):
    global S
    S.add(x)


def set_discard(x):
    global S
    S.discard(x)

# function dictionary (한번 써봤다)
cmd_switch = {'add': set_add, 'remove': set_discard, 'check': check_set,
              'toggle': toggle, 'all': set_all, 'empty': set_empty}

for _ in range(M):
    cmd = input_line().strip().split()
    if len(cmd) == 2:
        cmd_switch[cmd[0]](int(cmd[1]))
    else:
        S = cmd_switch[cmd[0]]()
