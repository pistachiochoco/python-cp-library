"""
dijkstra.py

Compute the shortest paths in a weighted graph.
"""

import heapq


def dijkstra(adj, s):
    """
    adj : Adjacency list: adj[u] = [(v, w), ...] means an edge u→v with weight w.
    s : Index of the starting node.
    """
    
    n = len(adj)
    dist = [float('inf')] * n
    dist[s] = 0
    hq = [(0, s)]

    while hq:
        d, cur = heapq.heappop(hq)
        if d > dist[cur]:
            continue
        for nxt, w in adj[cur]:
            nd = d + w
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(hq, (nd, nxt))
    return dist

if __name__ == "__main__":
    n, m, s = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        adj[u].append((v, d))

    dist = dijkstra(adj, s)
    for d in dist:
        if d == float('inf'):
            print("INF")
        else:
            print(d)