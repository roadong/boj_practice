import sys

input_line = sys.stdin.readline

# config.sys
# config.inf
# configures

N = int(input_line())

files = [list(input_line().rstrip()) for _ in range(N)]
file_len = len(files[0])

result = ''
if N == 1:
    print(''.join(files[0]))
else:
    for i in range(file_len):
        compare = files[0][i]
        for c in [j[i] for j in files]:
            if compare != c:
                result += '?'
                break
        if len(result) == i:
            result += compare
    print(result)


