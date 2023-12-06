import sys

input = lambda: (lambda x: x().rstrip())(sys.stdin.readline)

n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))


points = sorted(points)
sum_points = 0
start_point, end_point = points[0][0], points[0][1]
for i in range(1, n):
    if points[i][0] > end_point:
        sum_points += end_point - start_point
        start_point = points[i][0]
        end_point = points[i][1]
    elif points[i][1] > end_point:
        end_point = points[i][1]
    else:
        continue

sum_points += end_point - start_point

print(sum_points)
