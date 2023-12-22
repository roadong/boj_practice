import sys

input_line = sys.stdin.readline

color_info = {'black': 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8,
              "white": 9}

one_color = input_line().rstrip()
two_color = input_line().rstrip()
three_color = input_line().rstrip()

mid_result = int(color_info.get(one_color).__str__() + color_info.get(two_color).__str__())
print(mid_result * (10 ** color_info.get(three_color)))