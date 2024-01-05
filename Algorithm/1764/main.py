import sys

input_line = sys.stdin.readline

N, M = map(int, input_line().split())
dic = dict()
for _ in range(N + M):
    name = input_line().rstrip()
    if not dic.get(name):
        dic.update({name: 1})
    else:
        dic.update({name: 2})


result = []
for key, value in dic.items():
    if value == 2:
        result.append(key)

# 사전 순 정리
result.sort()
# prefix인 경우는 짧은 순으로
# result.sort(key=lambda x: len(x))

print(len(result))
for dbj in result:
    print(dbj)
