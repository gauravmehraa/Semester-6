from nltk.corpus import stopwords

# run once to download all stopwords 
# nltk.download('stopwords')

def stopword_removal(text):
  stopwords_set = set(stopwords.words('english'))
  cleaned = ''.join(char for char in text if char.isalnum() or char.isspace())
  tokens = cleaned.lower().split()
  filtered_tokens = [token for token in tokens if token not in stopwords_set]
  return ' '.join(filtered_tokens)

original = 'Alan Mathison Turing (23 June 1912 to 7 June 1954) was an English mathematician, computer scientist, logician, cryptanalyst, philosopher and theoretical biologist. He was highly influential in the development of theoretical computer science, providing a formalisation of the concepts of algorithm and computation with the Turing machine, which can be considered a model of a general-purpose computer. Turing is widely considered to be the father of theoretical computer science.'
# can also use file handling to read and write
print(stopword_removal(original))