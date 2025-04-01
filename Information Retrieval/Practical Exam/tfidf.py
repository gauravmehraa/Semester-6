import math
import numpy as np
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity

def get_tokens(tfs):
  tokens = set()
  for tf in tfs: tokens.update(tf.keys())
  return sorted(tokens)

def get_df(tfs, tokens):
  df = defaultdict(int)
  for token in tokens:
    for tf in tfs:
      if tf[token] > 0: df[token] += 1
  return df

def get_idf(dfs, n):
  idf = {}
  for token, df in dfs.items():
    idf[token] = round(math.log10(n / df) if df > 0 else 0.0, 2)
  return idf

def get_tfidf(tf, idf):
  tfidf = {}
  for token, freq in tf.items():
    tfidf[token] = round(math.log10(freq + 1) * idf.get(token, 0.0), 2)
  return tfidf

tfs = [
  { 'blue': 1, 'bright': 0, 'sky': 1, 'sun': 0 },
  { 'blue': 0, 'bright': 1, 'sky': 0, 'sun': 1 },
  { 'blue': 0, 'bright': 1, 'sky': 1, 'sun': 1 },
  { 'blue': 0, 'bright': 1, 'sky': 0, 'sun': 2 },
]
n = len(tfs)

tokens = get_tokens(tfs)
dfs = get_df(tfs, tokens)
idf = get_idf(dfs, n)
tfidf = [get_tfidf(tf, idf) for tf in tfs]

for i, weight in enumerate(tfidf):
  score = sum(weight.values())
  print(f"Doc {i+1} TF-IDF: {weight}")
  print(f"Doc {i+1} Score: {score}\n")

vectors = []
for doc in tfidf:
  vector = [doc.get(token, 0.0) for token in tokens]
  vectors.append(vector)

vectors = np.array(vectors)
cos_sim_matrix = cosine_similarity(vectors)
print("Cosine Similarity Matrix:")
print(cos_sim_matrix)