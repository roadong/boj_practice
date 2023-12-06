import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

txt = list(input())
tmp = []
for i in range(1, len(txt) - 1):
    for j in range(i + 1, len(txt)):
        a = txt[:i]
        b = txt[i:j]
        c = txt[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(''.join(a + b + c))

print(sorted(tmp)[0])
