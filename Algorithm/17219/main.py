from sys import stdin

input_line = stdin.readline


N, M = map(int, input_line().rstrip().split())
dic_table = dict()

for _ in range(N):
    site, ps = map(str, input_line().rstrip().split())
    dic_table.update({site: ps})

for _ in range(M):
    q = input_line().rstrip()
    print(dic_table.get(q))