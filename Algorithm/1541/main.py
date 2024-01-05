import sys
from collections import deque

input_line = sys.stdin.readline

min_problem = input_line().rstrip()

# 숫자, 기호 분할
operator = []
number_list = []
# parsing
num_basket = ''
for i in min_problem:
    if i in ['+', '-']:
        operator.append(i)
        number_list.append(int(num_basket))
        num_basket = ''
    else:
        num_basket += i

if len(num_basket) > 0:
    number_list.append(int(num_basket))

result = number_list[0]

for i in range(1, len(number_list)):
    if operator[i - 1] == '+':
        result += number_list[i]
    else:
        result -= sum(number_list[i:])
        break

print(result)


