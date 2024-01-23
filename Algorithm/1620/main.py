from sys import stdin

input_line = stdin.readline

N, M = map(int, input_line().rstrip().split())
pokemon_dict = {}
for i in range(1, N + 1):
    pokemon_name = input_line().rstrip()
    pokemon_dict.update({str(i): pokemon_name})
    pokemon_dict.update({pokemon_name: i})

for _ in range(M):
    q = input_line().rstrip()
    print(pokemon_dict.get(q))

