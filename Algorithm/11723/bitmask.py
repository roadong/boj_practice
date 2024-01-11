import sys

input_line = sys.stdin.readline

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

# AND (&) : 해당 비트가 있나?
# OR (|) : 해당 비트를 합친다
# XOR (^) : 해당 비트가 다른 위치에 1?
# 비트 마스킹 기법을 한번 써 먹어보자
M = int(input_line())
S = 0b0  # 0


def add_set(x):
    global S
    # 집합에 OR 연산 해주면 된다
    S |= (1 << x)


def remove_set(x):
    global S
    # 집합에 AND 연산 (있으면 0 없어도 불일치 0)
    S &= ~(1 << x)


def toggle_set(x):
    global S
    # 집합에 XOR 연산 (없으면 1 있으면 0)
    S ^= (1 << x)


def check_set(x):
    global S
    print(1 if S & (1 << x) else 0)


cmd_switch = {
    'add': add_set,
    'remove': remove_set,
    'toggle': toggle_set,
    'check': check_set,
    'all':  (1 << 21) - 1,
    'empty': 0b0
}

for _ in range(M):
    cmd_set = input_line().strip().split()

    if len(cmd_set) == 2:
        cmd, num = cmd_set
        cmd_switch[cmd](int(num))
    else:
        # 명령어만 들어있으면 채우거나 비우는 것 밖에 없다
        S = cmd_switch[cmd_set[0]]
