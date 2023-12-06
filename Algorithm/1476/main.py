E, S, M = map(int, input().split())
e = 1
s = 1
m = 1
year = 1

def counter(earth, sun, moon):
    return 1 if earth == 15 else earth + 1, 1 if sun == 28 else sun + 1, 1 if moon == 19 else moon + 1


while True:
    if e == E and s == S and m == M:
        break
    e, s, m = counter(e, s, m)
    year += 1

print(year)
