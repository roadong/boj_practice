# 빠른 구간 합 및 탐색 (인덱스 & 비트연산)
# i & -i => 마지막 비트가 1인 것 구하기 (음수인 자기 자신은 마지막을 1을 제외하고 전부 인버스)
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.fenwickTree = [[0] * (size + 1)]

    def bit_sum(self, idx):
        temp = 0
        while idx:
            temp += self.fenwickTree[idx]            
            idx -= idx & -idx

        return temp

    def update(self, idx, diff):
        while idx <= self.size:
            self.fenwickTree[idx] += diff
            # 다음 구간 인덱스
            idx += idx & -idx

    def range_sum(self, left, right):
        return self.bit_sum(right) - self.bit_sum(left - 1)

    # def find(self, left, idx, right):
    #     idx_sum = self.bit_sum(idx)
    #     if idx_sum == left and self.check[idx]:
    #         return idx
    #     if idx_sum < left:
    #         return self.find(left, idx + (1 << right), right - 1)
    #     return self.find(left, idx - (1 << right), right - 1)
