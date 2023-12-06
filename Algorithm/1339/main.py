import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

N = int(input())
alphabet = [0 for i in range(ord('Z') - 64)]


def find_alphabet_index(s):
    return ord(s) - 65


for _ in range(N):
    arr = list(input())
    index = len(arr) - 1
    for i in range(len(arr)):
        alphabet[find_alphabet_index(arr[i])] += 10 ** index
        index -= 1


alphabet.sort(reverse=True)
num = 9
result = 0
for i in range(10):
    result += alphabet[i] * num
    num -= 1

print(result)
