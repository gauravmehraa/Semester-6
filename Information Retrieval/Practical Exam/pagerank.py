import numpy as np

def pagerank(graph, beta):
  nodes = list(graph.keys())
  n = len(nodes)
  positions = { node: index for index, node in enumerate(nodes) }

  adjacency = np.zeros((n, n))
  chances = np.ones((n, n)) / n

  for source, destinations in graph.items():
    for destination in destinations:
      adjacency[positions[destination], positions[source]] = 1

  column_sums = adjacency.sum(axis=0) # column
  for col in range(n):
    if column_sums[col] == 0: # no outgoing link
      adjacency[:, col] = 1 / n
    else:
      adjacency[:, col] /= column_sums[col]

  matrix = (beta * adjacency) + ((1 - beta) * chances)
    
  ranks = np.ones(n) / n
  while True:
    new_ranks = matrix.dot(ranks)
    if np.linalg.norm(new_ranks - ranks, 1) < 0.000001: break
    ranks = new_ranks
  
  for i, node in enumerate(nodes): print(f"{node}: {ranks[i]:.2f}")

graph = {
  'y': ['y', 'a'],
  'a': ['y', 'm'],
  'm': ['a'],
}
beta = 0.85
pagerank(graph, beta)
