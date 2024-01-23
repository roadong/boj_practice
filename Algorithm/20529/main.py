from itertools import combinations
import sys

input_line = sys.stdin.readline


t = int(input_line().rstrip())
for idx in range(t):
    n = int(input_line())
    temp = input_line().split()
    # 전혀 다른 성격으로 16가지를 채우면 17번째 부턴
    # 2번 겹치는 게 하나 나온다 마찬가지로
    # 33번째 부턴 어떤게 들어오던 간에 3개가 겹친다
    if n > 32:
        print(0)
        continue
    else:
        # 리스트를 3개 조합으로 구성
        temp = list(combinations(temp, 3))
        score_list = []
        for compare in temp:
            score = 0
            for idx in range(4):
                # 같은 조합인 경우 pass
                if (compare[0][idx] == compare[1][idx]
                        and compare[0][idx] == compare[2][idx]
                        and compare[1][idx] == compare[2][idx]):
                    continue

                score += 2
            score_list.append(score)
        print(min(score_list))
