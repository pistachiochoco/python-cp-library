"""
zero_one_bfs.py

Compute shortest paths in a graph whose edge weights are only 0 or 1.

Time Complexity: O(N + M)
Space Complexity: O(N)
"""

from collections import deque


INF = float("inf")


def zero_one_bfs(adj, s):
    """
    adj : Adjacency list: adj[u] = [(v, w), ...] means an edge u->v with weight w.
          Each weight w must be 0 or 1.
    s : Index of the starting node.
    """

    n = len(adj)
    dist = [INF] * n
    dist[s] = 0
    dq = deque([s])

    while dq:
        cur = dq.popleft()
        for nxt, w in adj[cur]:
            nd = dist[cur] + w
            if dist[nxt] <= nd:
                continue

            dist[nxt] = nd
            if w == 0:
                dq.appendleft(nxt)
            else:
                dq.append(nxt)

    return dist


if __name__ == "__main__":
    n, m, s = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())

        # Undirected Graph
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = zero_one_bfs(adj, s)
    for d in dist:
        if d == INF:
            print("INF")
        else:
            print(d)
