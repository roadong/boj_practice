import sys

input_line = sys.stdin.readline

N = int(input_line())

atm_time = list(map(int, input_line().rstrip().split(' ')))

# 맨앞에 적게 걸리는 사람이 와야 누적이 최소가 된다
atm_time.sort()

result = 0
for i in range(N):
    result += sum(atm_time[:i + 1])

print(result)
