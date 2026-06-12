# 前処理: O(N log N)
# LCAクエリ: O(log N)
# 距離クエリ: O(log N)
# メモリ: O(N log N)

from collections import deque

class LCA:
    def __init__(self, n):
        self.n = n
        self.LOG = n.bit_length()
        self.g = [[] for _ in range(n)]
        self.depth = [-1] * n
        self.parent = [[-1] * n for _ in range(self.LOG)]

    def add_edge(self, u, v):
        """0-indexの無向辺を追加"""
        self.g[u].append(v)
        self.g[v].append(u)

    def build(self, root=0):
        """rootを根として前処理"""
        q = deque([root])
        self.depth[root] = 0

        while q:
            v = q.popleft()

            for nv in self.g[v]:
                if self.depth[nv] != -1:
                    continue
                
                self.depth[nv] = self.depth[v] + 1
                self.parent[0][nv] = v
                q.append(nv)

        for k in range(1, self.LOG):
            for v in range(self.n):
                p = self.parent[k - 1][v]
                if p != -1:
                    self.parent[k][v] = self.parent[k - 1][p]

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        diff = self.depth[u] - self.depth[v]

        for k in range(self.LOG):
            if (diff >> k) & 1:
                u = self.parent[k][u]
        
        if u == v:
            return u
        
        for k in range(self.LOG - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        
        return self.parent[0][u]

    def dist(self, u, v):
        """uとvの木上距離"""
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]

    def kth_ancestor(self, v, k):
        """vのk個上の祖先を返す。存在しないなら-1"""
        for i in range(self.LOG):
            if k >> i & 1:
                v = self.parent[i][v]
                if v == -1:
                    return -1
        return v


if __name__ == "__main__":
    n = 5
    tree = LCA(n)

    tree.add_edge(0, 1)
    tree.add_edge(0, 2)
    tree.add_edge(1, 3)
    tree.add_edge(1, 4)

    tree.build(root=0)

    print(tree.lca(3, 4))   # 1
    print(tree.lca(3, 2))   # 0
    print(tree.dist(3, 2))  # 3
