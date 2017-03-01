# 22 Elementary Graph Algorithms

Searching a graph means systematically following the edges of the graph so as to visit the vertices of the graph. A graph-searching algorithm can discover much about the structure of the graph.

## 22.1 Representations of graphs

We can choose between two standard way to represent a graph G = (V, E):

* As collections of adjacency lists
* As adjacency matrices

Either way applies to both directed and undirected graphs. Because the adjacency-list representation provides a compact way to represent *sparse* graphs—those for which |E| is much less than |V|<sup>2</sup>—it is usually the method of choice.

```
Figure 22.1 Two representations of an undirected graph

① -----② 
|     / | \
|   /   |  ③
| /     | /
⑤------④ 
(a) An undirected graph G with 5 vertices and 7 edges

1 ▢→ 2 → 5 → /
2 ▢→ 1 → 5 → 3 → 4 /
3 ▢→ 2 → 4 /
4 ▢→ 2 → 5 → 3 /
5 ▢→ 4 → 1 → 2 /

    1 2 3 4 5
   ----------
1 | 0 1 0 0 1
2 | 1 0 1 1 1
3 | 0 1 0 1 0
4 | 0 1 1 0 1
5 | 1 1 0 1 0

```

...much omitted...
### Exercises

**22.1-1**

Calculating the out-degrees would require Θ(|V| + |E|) time, while the in-degrees would require Θ(|V||E|) time.

**22.1-2**
 
```
       ①
      /   \
   ②       ③
  /  \    /   \
 ④   ⑤  ⑥    ⑦
```
