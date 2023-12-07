# Quick-Find
# Quick-Union
# Union by size / rank
# Path compression

class DisjointSet:
    def __init__(self, n):
        # 각 인덱스에 저장된 값은 해당 요소의 부모 노드 인덱스를 가리키는 리스트
        self.parentIndexes = [i for i in range(n)]

    def find(self, node):
        # 루트가 자기 자신인 경우 자신을 가리키는 예외 처리
        if self.parentIndexes[node] == node:
            return node

        # 그룹에 포함된 노드인덱스에 루트 노드 인덱스 값을 넣어준다
        # path compression
        self.parentIndexes[node] = self.find(self.parentIndexes[node])
        return self.parentIndexes[node]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        # 이미 그룹화 됨
        if u == v:
            return False

        if u < v:
            self.parentIndexes[v] = u
        else:
            self.parentIndexes[u] = v

        return True
