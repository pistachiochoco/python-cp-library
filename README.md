# python-cp-library
snippets and templates for competitive programming in Python for personal use


### Algo/
- [Dutch National Flag Algorithm](algo/dutch_national_flag.py): In-place sorting of arrays with 0s, 1s, and 2s.

### Graph/
- [Dijkstra](graph/dijkstra.py): Shortest paths in graphs with non-negative edge weights.
- [0-1 BFS](graph/zero_one_bfs.py): Shortest paths in graphs with edge weights 0 or 1.

#### Dijkstra vs 0-1 BFS
| Algorithm | Edge weights | Use when | Time complexity |
| --- | --- | --- | --- |
| [Dijkstra](graph/dijkstra.py) | Non-negative weights | Edge weights are general non-negative values. | O((N + M) log N) |
| [0-1 BFS](graph/zero_one_bfs.py) | 0 or 1 only | Every edge weight is 0 or 1. | O(N + M) |
