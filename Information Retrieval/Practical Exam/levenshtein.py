def levenshtein_distance(s1, s2):
  rows, cols = len(s2) + 1, len(s1) + 1
  grid = [[0 for _ in range(cols)] for _ in range(rows)]

  for i in range(1, rows): grid[i][0] = i
  for j in range(1, cols): grid[0][j] = j

  for i in range(1, rows):
    for j in range(1, cols):
      deletion = grid[i-1][j] + 1
      insertion = grid[i][j-1] + 1
      substitution = grid[i-1][j-1] + (0 if s1[j-1] == s2[i-1] else 1)
      grid[i][j] = min(deletion, min(insertion, substitution))
  return grid[-1][-1]
    
s1 = "execution"
s2 = "intention"
distance = levenshtein_distance(s1, s2)
print(f"Levenshtein Distance: {distance}")