import heapq
import sys

input_line = sys.stdin.readline

T = int(input_line())
result = []


# I : num을 큐에 삽입, D 1: 최대값 삭제, D -1: 최소값 삭제
def process(q):
    min_queue, max_queue = [], []
    visited = [False] * (q + 1)

    for i in range(q):
        (command, num) = map(str, input_line().rstrip().split(' '))
        if command == 'I':
            heapq.heappush(min_queue, (int(num), i))
            heapq.heappush(max_queue, (-int(num), i))
            # 삽입한 후에 동기화 하지 않은 노드 체크
            visited[i] = True
        else:
            # visited -> False는 동기화가 끝난 노드
            # 동시에 동기화가 되지 않는다
            if num == '-1':
                # 최대힙에서 이미 정리된 노드가 최소값이지 않게 정리 
                while min_queue and not visited[min_queue[0][1]]:
                    heapq.heappop(min_queue)
                if min_queue:
                    # 해당 노드까지 동기화가 끝남을 표시
                    visited[min_queue[0][1]] = False
                    # 해당 명령을 수행한다
                    heapq.heappop(min_queue)
            else:
                # 최소힙에서 이미 정리된 노드가 최대값이지 않게 정리
                while max_queue and not visited[max_queue[0][1]]:
                    heapq.heappop(max_queue)
                if max_queue:
                    visited[max_queue[0][1]] = False
                    # 해당 명령을 수행
                    heapq.heappop(max_queue)

    # 한쪽만 동기화 되었기 때문에 한번 더 정리 
    while min_queue and not visited[min_queue[0][1]]:
        heapq.heappop(min_queue)
    while max_queue and not visited[max_queue[0][1]]:
        heapq.heappop(max_queue)

    return f'{-max_queue[0][0]} {min_queue[0][0]}' if max_queue and min_queue else 'EMPTY'


for _ in range(T):
    Q = int(input_line())
    result.append(process(Q))


for item in result:
    print(item)
