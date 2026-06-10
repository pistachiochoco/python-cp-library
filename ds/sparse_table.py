# 前処理: O(NlogN)
# クエリ: O(1)
# 更新: できない

class SparseTable:
    def __init__(self, arr, op=min):
        self.op = op
        self.n = len(arr)

        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1

        self.st = [arr[:]]

        k = 1
        while (1 << k) <= self.n:
            prev = self.st[k - 1]
            length = 1 << k
            half = 1 << (k - 1)

            row = []
            for i in range(self.n - length + 1):
                row.append(op(prev[i], prev[i + half]))

            self.st.append(row)
            k += 1

    # [l, r)
    def query(self, l, r):
        k = self.log[r - l]
        length = 1 << k
        return self.op(self.st[k][l], self.st[k][r - length])
    


# Library Checker: https://judge.yosupo.jp/problem/staticrmq

import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

sp = SparseTable(A, min)

ans = []

for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(str(sp.query(l, r)))

print("\n".join(ans))