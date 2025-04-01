from collections import defaultdict
import math

def get_tokens(tfs):
  tokens = set()
  for tf in tfs: tokens.update(tf.keys())
  return tokens

def get_logf(tf):
  logf = {}
  for token, freq in tf.items():
    logf[token] = 0.0 if freq == 0 else round((math.log10(freq) + 1), 2)
  return logf

def normalize(logf):
  factor = math.sqrt(sum(val * val for val in logf.values()))
  normalized = {}
  for token, val in logf.items():
    normalized[token] = round(val / factor, 2) if factor != 0 else 0.0
  return normalized

def build_vectors(normalized, tokens):
  vectors = []
  for norm in normalized:
    vector = [norm.get(token, 0.0) for token in tokens]
    vectors.append(vector)
  return vectors

def cosine_similarity(vec1, vec2):
  dot = sum(a * b for a, b in zip(vec1, vec2))
  norm1 = math.sqrt(sum(a * a for a in vec1))
  norm2 = math.sqrt(sum(b * b for b in vec2))
  if norm1 == 0 or norm2 == 0: return 0.0
  return round(dot / (norm1 * norm2), 2)

tfs = [
  { 'reaction': 15, 'params': 25, 'vehicle': 0, 'synthesize': 16, 'fast': 1 },
  { 'reaction': 0, 'params': 5, 'vehicle': 20, 'synthesize': 2, 'fast': 1 },
  { 'reaction': 3, 'params': 2 , 'vehicle': 11, 'synthesize': 0, 'fast': 19 },
]
n = len(tfs)

tokens = get_tokens(tfs)
logfs = [get_logf(tf) for tf in tfs]
normalized = [normalize(logf) for logf in logfs]
vectors = build_vectors(normalized, tokens)

for i in range(n):
  for j in range(i + 1, n):
    sim = cosine_similarity(vectors[i], vectors[j])
    print(f"Doc {i+1} and Doc {j+1}: {sim}")
