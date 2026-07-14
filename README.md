# python-cp-library
snippets and templates for competitive programming in Python for personal use


### Algo/
- [Dutch National Flag Algorithm](algo/dutch_national_flag.py): In-place sorting of arrays with 0s, 1s, and 2s.

### DS/
- [Fenwick Tree](ds/fenwick_tree.py): Point add and range sum queries.
- [Fenwick Tree XOR](ds/fenwick_tree_xor.py): Point xor and range xor queries.
- [Fenwick Tree Prefix Min](ds/fenwick_tree_prefix_min.py): Prefix minimum queries with monotonic updates.
- [Fenwick Tree Prefix Max](ds/fenwick_tree_prefix_max.py): Prefix maximum queries with monotonic updates.

### Graph/
- [Dijkstra](graph/dijkstra.py): Shortest paths in graphs with non-negative edge weights.
- [0-1 BFS](graph/zero_one_bfs.py): Shortest paths in graphs with edge weights 0 or 1.

#### Dijkstra vs 0-1 BFS
| Algorithm | Edge weights | Use when | Time complexity |
| --- | --- | --- | --- |
| [Dijkstra](graph/dijkstra.py) | Non-negative weights | Edge weights are general non-negative values. | O((N + M) log N) |
| [0-1 BFS](graph/zero_one_bfs.py) | 0 or 1 only | Every edge weight is 0 or 1. | O(N + M) |
