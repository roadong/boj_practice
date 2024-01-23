from sys import stdin

input_line = stdin.readline

N = int(input_line().rstrip())

x_list = list(map(int, input_line().rstrip().split()))
hashing_index = {}
set_x = sorted(list(set(x_list)))
for i in range(len(set_x)):
    hashing_index.update({set_x[i]: i})

result = []
for i in x_list:
    result.append(hashing_index.get(i))

print(*result)