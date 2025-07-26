"""
floyd_warshall.py

Compute all-pairs shortest paths using the Floyd-Warshall algorithm.

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

INF = float('inf')

def floyd_warshall(n, dist):
    """
    Parameters:
    -----------
    n : Number of vertices (0..n-1)
    dist : Adjacency matrix where dist[i][j] is the direct cost from i to j, INF if no edge, and 0 if i == j.

    Returns:
    --------
    The same matrix 'dist', updated in-place so that dist[i][j] is the shortest distance from i to j.
    """

    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    return dist


if __name__ == "__main__":
    n, m = map(int, input().split())
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        
    for _ in range(m):
        u, v, w = map(int, input().split())
        dist[u][v] = min(dist[u][v], w)

    dist = floyd_warshall(n, dist)
    for d in dist:
        print(d)