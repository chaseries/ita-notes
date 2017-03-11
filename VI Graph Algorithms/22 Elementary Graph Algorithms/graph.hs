-- Implementation of an adjacency list representation of a graph

data Vertex v = Vertex v
  deriving (Show)

type Edges v = [Vertex v]

type AdjList v = [Edges v]

data Graph v = Graph (AdjList v)
  deriving (Show)


