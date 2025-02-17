# Practical 2 - Incidence Matrix and Evaluation of AND/OR query
from nltk.corpus import stopwords
def stopword_removal(originalfile, newfile):
    stop_words = set(stopwords.words('english'))
    with open(originalfile) as f:
        text = f.read()
        data = ''.join(char for char in text if char.isalnum() or char.isspace())
        tokens = data.lower().split()
    
    with open (newfile, 'w') as f:
        data = [token for token in tokens if token not in stop_words]
        f.write(' '.join(data))

def incidence_matrix(n):
    global positions
    matrix = []
    words = []
    text = []
    seen = set()
    for i in range(1, 6):
        new_file = f"filtered{i}.txt"
        stopword_removal(f"raw{i}.txt", new_file)
        
        with open(new_file, 'r') as f:
            data = f.read().split()
            text.append(data)
            for word in data:
                if word not in seen: words.append(word)
                seen.add(word)

    row = 0
    for word in words:
        frequency = []
        for i in range(5):
            frequency.append(1 if word in text[i] else 0)
        matrix.append([word] + frequency)
        positions[word] = row
        row += 1

    return matrix

def search(query, matrix):
    global positions
    n = len(matrix[0]) - 1 # minus one as first element is word
    
    terms = query.split()[0::2]
    operators = query.split()[1::2]
    
    rows = []
    for term in terms:
        rownumber = positions.get(term)
        if rownumber is None: rows.append([0 for _ in range(n)])
        if rownumber is not None: rows.append(matrix[rownumber][1:])
    
    result = rows[0]
    if len(rows) == 1: return result 

    current = 0
    for row in rows[1:]:
        for i in range(n):
            if operators[current] == "AND": result[i] &= row[i]
            if operators[current] == "OR": result[i] |= row[i]
        if current < len(operators) - 1: current += 1
    return result

positions = {}
matrix = incidence_matrix(5)
query = "turing OR hello AND computer"
result = search(query, matrix)
print(f"Query: {query}")
print(f"Result: {result}")


# N-Grams
def ngrams(sentence, n):
    result = []
    words = [f"${word}$" for word in sentence.split(" ")]
    for word in words:
        for i in range(len(word)-n+1):
            result.append(word[i:i+n])
    return result

# Practical 5 - Levenshtein Distance

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
s2 = "intention" #ans = 5

# Practical 7 - Porter Stemmer
from nltk.stem import PorterStemmer

def stem(sentence):
    words = sentence.split()
    stemmer = PorterStemmer()
    result = [stemmer.stem(word) for word in words]
    return ' '.join(result)

# Practical 9 - Page Rank Algorithm
from collections import defaultdict

def multiply(matrix, vector):
    result = [0 for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
            result[i] = round(result[i], 2)
    return result

def adjacency_matrix(graph):
    n = len(graph)
    nodes = list(graph.keys())
    positions = { node: index for index, node in enumerate(nodes) }
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for source, destinations in graph.items():
        for destination in destinations:
            matrix[positions[destination]][positions[source]] = 1
    return matrix

def chance_matrix(graph):
    n = len(graph)
    matrix = [[1/n for _ in range(n)] for _ in range(n)]
    return matrix

def pagerank(graph, beta=0.8):
    n = len(graph)
    matrix = adjacency_matrix(graph)
    chances = chance_matrix(graph)
    nodes = list(graph.keys())
    positions = { index: node for index, node in enumerate(nodes) }

    for col in range(n):
        sum = 0
        for row in range(n): sum += matrix[row][col]
        if sum == 0: continue
        for row in range(n):
            matrix[row][col] /= sum
    
    for row in range(n):
        for col in range(n):
            matrix[row][col] *= beta
            matrix[row][col] += ((1 - beta) * chances[row][col])

    ranks = [0 for _ in range(n)]
    ranks[0] = 1
    while True:
        prev = ranks.copy()
        ranks = multiply(matrix, ranks)
        same = False
        for node in range(n):
            if ranks[node] != prev[node]: same = False
            else: same = True
        if same: break    

    for i in range(n): print(f"{positions[i]}: {ranks[i]}")

def add(graph, u, v): graph[u].append(v)

def main():
    graph = defaultdict(list)
    graph = {
        'y': ['y', 'a'],
        'a': ['y', 'm'],
        'm': ['m'],
    }
    pagerank(graph, 0.85)

main()