# $\fbox{Chapter 6: GRAPHS}$





### <u>Types of Graphs</u>

- **<u>Simple graph</u>:** Maximum one edge connecting pair of vertices.
- **<u>Multigraph</u>:** Opposite of simple graph.
- **<u>Pseudo graph</u>:** Multigraph with loops.
- **<u>Mixed graph</u>:** Directed + Undirected
- **<u>Regular graph</u>:** Every vertex with same degree.
- **<u>Wheel graph</u>:** All vertices having degree 3 except the one in middle.
- **<u>N-cube</u>:** Bit length & dimensional changes.


### <u>Bipartite Graphs</u>

- **<u>Bipartite graph</u>:** Two sets of graph ($v1$ & $v2$). A vertex from $v1$ connects to $v2$ only.
- **<u>Complementary graphs</u>:** Non-bipartite graphs.


### <u>Adjacency Matrix</u>

- Make matrix with column & rows with vertices name.
- Write one if pair exists.
- Its different for directed and undirected graphs.


### <u>Indices Matrix</u>

- Make matrix with vertices as row & column as edges.
- It is also different for directed and undirected graphs.


### <u>Isomorphism Graphs</u>

#### Properties:

- Same number of vertices.
- Same number of edges.
- Equal degree of each vertex.
- Correspondence of edges are same.


### <u>Graphical Terms</u>

- **<u>Walk</u>:** Random traversing vertex to vertex.
- **<u>Trail</u>:** Edge can’t be repeated when traversing.
- **<u>Circuit</u>:** (Trail + Start) & end vertex are same
- **<u>Path</u>:** Neither vertex nor edge can be repeated.
- **<u>Cycle</u>:** (Path + Start) & end vertex are same
- **<u>Trivial walk</u>:** Traversing in isolated graph (non-sensical).
- **<u>K-cycle</u>:** $K$ is length.
- **<u>Connected graph</u>:** Path in undirected graph.
- **<u>Connected component</u>:** Subgraph of connected graph.
- **<u>Cut vertex</u>:** Removing a vertex and its related edges.
- **<u>Strongly connected</u>:** Bidirectional path.
- **<u>Weakly connected</u>:** Non-bidirectional path.


### <u>Eulerian Graph Terms</u>

- Its all about edges.
- **<u>Eulerian circuit</u>:** A circuit containing all edges of a graph.
- **<u>Eulerian path</u>:** Path containing all edges.
- **<u>Eulerian graph</u>:** Connected Eulerian circuit.


### <u>Hamiltonian Graph Terms</u>

- Its all about vertices.


### <u>Special Algorithms</u>

- **<u>Dijkstra’s Algorithm</u>:** Fix and find connective paths.
- **<u>Chromatic colouring</u>:** Least number of colours required for a graph.

#### Kruskal’s Algorithm:

  - Keep choosing edge with minimum edge.
  - Don’t end up making a circuit.
  - Stop after $(n-1)$ edges ($n$ is number of edges).

#### Prim’s Algorithm:

  - Select any vertex, and then its smallest edge.
  - Choose next smallest edge from there.
  - Don’t end up making a circuit.
  - Continue until all vertices included.


### <u>Unique to Software Engineering</u>

- **<u>Dense graph</u>:** Edges are more than vertices.
- **<u>Sparse graph</u>:** Edges are less than vertices.


### <u>Breadth First Search (BFS)</u>

- Contains two queues - Visited & Queued
- Visit each node one by one.
- Push each visited and neighbor node to Visited.
- Push `0` to Queue at first.
- Then push unvisited neighbors in Queue.
- Now repeat it by dequeuing first element at each iteration.

---
