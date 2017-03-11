# 22 Elementary Graph Algorithms

This chapter presents methods for representing a graph and for searching a graph. *Searching a graph means systematically following the edges of the graph so as to visit the vertices of the graph*. A graph-searching algorithm can discover much about the structure of the graph.

## 22.1 Representations of graphs

We can choose between two standard way to represent a graph *G* = (*V*, *E*):

* As collections of adjacency lists
* As adjacency matrices

Most of the graph algorithms presented in this book assume that an input graph is reprsented in adjacency-list form; we may prefer an adjacency matrix when a graph is *dense*.

Either way applies to both directed and undirected graphs. Because the adjacency-list representation provides a compact way to represent *sparse* graphs—those for which |*E*| is much less than |*V*|<sup>2</sup>—it is usually the method of choice.

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

The *adjacency list representation* of a graph *G* = (*V*, *E*) consists of an array *Adj* of |*V*| lists, one for each vertex in |*V*|. For each *u* ∈ *V*, the adjacency list Adj[u] contains all the vertices *v* such that there is an edge (*u*, *v*) ∈ *E*. That is, *Adj*[*u*] consists of all the vertices adjacent to *u* in *G*.

If *G* is a directed graph, the sum of the lengths of all the adjacency lists is |*E*|, since an edge of the form (*u*, *v*) is represented by having *v* appear in *Adj*[*u*]. If *G* is undirected, the sum of the lengths of all adjacency lists is 2|*E*|.

We can readily adapt adjacency lists to represent *weighted graphs*, that is, graphs for which each edge has an associated *weight*, typically given by a *weight function* *w* : *E* → ℝ. We simply store the weight *w*(*u*, *v*) of the edge (*u*, *v*) ∈ *E* with vertex *v* in *u*'s adjacency list.

For the *adjacency matrix representation* of a graph *G* = (*V*, *E*), we assume that the vertices are numbered 1,2,...,|*V*| in some arbitrary manner. Then the adjacency matrix representation of a graph *G* consists of a |*V*| × |*V*| matrix *A* = (A<sub>ij</sub>) such that 

    -- Pseudohaskell
    a (i, j) | (i, j) ∈ E = 1
             | otherwise = 0

An adjacency matrix can also represent a weighted graph. For example, *G* = (*V*, *E*) is a weighted graph with edge-weight function *w*. We can simply store the weight *w*(*u*, *v*) of the edge (*u*, *v*) ∈ *E* as the entry in row *u* and column *v* of the adjacency matrix. If an edge does not exist, we can store a NIL value in its corresponding matrix entry (though for many problems it is convenient to use a value such as 0 or ∞).

### Exercises

**22.1-1**

Calculating the out-degrees would require Θ(|V| + |E|) time, while the in-degrees would require Θ(|V||E|) time.

**22.1-2**
 
```
       ①
     /    \
   ②       ③
  /  \    /   \
 ④   ⑤  ⑥    ⑦

{ 1: [2,3] 
, 2: [1,4,5]
, 3: [1,6,7]
, 4: [2]
, 5: [2]
, 6: [3]
, 7: [3]
}

   1 2 3 4 5 6 7
1  0 1 1 0 0 0 0
2  1 0 0 1 1 0 0
3  1 0 0 0 0 1 1
4  0 1 0 0 0 0 0
5  0 1 0 0 0 0 0
6  0 0 1 0 0 0 0
7  0 0 1 0 0 0 0
```

## 22.2 Breadth-first search

Breadth-first search is one of the simplest algorithms for searching a graph and the archetype for many important graph algorithms. Breadth-first search is so-named because it expands the frontier between discovered and undiscovered vertices uniformly across the breadth of the frontier. That is, the algorithm discovers all vertices at distance *k* from *s* before discovering any vertices at distance *k* + 1.

Given a graph *G = (V, E)* and a distinguished *source* vertex *s*, breadth-first search:

* systematically explores the edges of *G* to "discover" every vertex that is reachable from *s*.
* Computes the distance (smallest number of edges) from *s* to each reachable vertex.
* Produces a "breadth-first tree" with root *s* that contains all reachable vertices. (For any vertex *v* reachable from *s*, the simple path in the breadth-first tree from *s* to *v* corresponds to a "shortest path" from *s* to *v* in *G*.)

### Definitions
*Sparse graph* Those graphs for which |*E*| (that is, the total number of edges) is much less than |*V*|<sup>2</sup> (that is, the total number of vertices squared).
*Dense graph* Those graphs for which |*E*| is close to |*V*|<sup>2</sup>.
*Weighted graph*
