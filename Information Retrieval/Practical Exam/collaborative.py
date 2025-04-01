import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def find_similar_users(user_id, data, k, positions):
  k += 1 # user itself will also be counted
  user = data.loc[user_id].values.reshape(1, -1) # get user's own ratings
  knn = NearestNeighbors(n_neighbors=k, algorithm="brute", metric="cosine").fit(data)
  distances, indices = knn.kneighbors(user, return_distance=True)
  return distances[0][1:], [positions[i] for i in indices[0][1:]] # skip first neighbor (the user itself)

def predict(ratings, user_id, movie_id, k):
  data = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
  users = ratings['userId'].unique() # list of user IDs
  positions = dict(zip(range(len(users)), users)) # maps row number to user ID

  if data.loc[user_id][movie_id] != 0:
    print("Rating already exists")
    return data.loc[user_id][movie_id]
  
  distances, similar_users = find_similar_users(user_id, data, k, positions)
  numerator = denominator = 0
  
  for distance, other_user in zip(distances, similar_users):
    rating = data.loc[other_user, movie_id]
    if rating:
      numerator += rating * distance
      denominator += distance

  if denominator == 0: # no other user has rated that movie
    print("Insufficient ratings")
    return None
  
  return numerator / denominator

data = {
  'userId':  [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9, 10, 10],
  'movieId': [1, 2, 1, 2, 3, 1, 2, 3, 1, 3, 1, 2, 3, 1, 3, 1, 2, 3, 1, 2, 1, 2, 3, 1,  3],
  'rating':  [4, 5, 5, 4, 3, 3, 2, 4, 4, 4, 2, 3, 5, 5, 2, 3, 4, 5, 4, 5, 3, 3, 3, 3,  4]
}
# ratings = pd.read_csv('ratings.csv')
# user_id, movie_id, k = 1, 69, 10

ratings = pd.DataFrame(data)
user_id, movie_id, k = 1, 3, 3

prediction = predict(ratings, user_id, movie_id, k)
print(f"Predicted Rating: {prediction}")