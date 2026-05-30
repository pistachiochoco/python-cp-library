import sys
input = sys.stdin.buffer.readline

class FenwickTree:
    def __init__(self, n) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i
    
    # [0, i)
    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
    
    # [l, r)
    def sum(self, l, r):
        return self._sum(r) - self._sum(l)


# Library Checker: https://judge.yosupo.jp/problem/point_add_range_sum
N, Q = map(int, input().split())
A = list(map(int, input().split()))

fw = FenwickTree(N)

for i, a in enumerate(A):
    fw.add(i, a)

ans = []

for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 0:
        fw.add(a, b)
    else:
        ans.append(str(fw.sum(a, b)))

print("\n".join(ans))