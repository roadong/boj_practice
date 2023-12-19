from collections import deque


class DAG:
    def __init__(self, size):
        self.degree = [0] * (size + 1)
        self.graph = [[] for _ in range(size + 1)]
        self.deque = deque()

    def setup_dag(self, edges_info, **kwargs):
        # DAG 그래프 생성 및 진입차수 계산
        for edge in edges_info:
            v, e = edge
            if v < e:
                self.graph[v].append(e)
                self.degree[e] += 1
            else:
                self.graph[e].append(v)
                self.degree[v] += 1

        # 진입차수가 0이면 큐에 집어넣고 대기
        for i in range(1, len(self.degree)):
            if self.degree[i] == 0:
                self.deque.append(i)

    def toplogy_sort(self):
        result = []
        while self.deque:
            sort_dedicate = self.deque.popleft()
            # 꺼내서 나온건 진입 차수가 0
            result.append(sort_dedicate)

            # 간선 제거
            for idx in self.graph[sort_dedicate]:
                idx: int
                self.degree[idx] -= 1
                # 간선을 제거 했더니 진입차수가 0이면 큐에 삽입
                if self.degree[idx] == 0:
                    self.deque.append(idx)

        return result


topology = DAG(5)
edges = [(1, 2), (2, 3), (3, 4), (1, 4), (4, 5)]
topology.setup_dag(edges)
print(topology.toplogy_sort())
