from nltk.stem import PorterStemmer

def stem(sentence):
  words = sentence.split()
  stemmer = PorterStemmer()
  result = [stemmer.stem(word) for word in words]
  return ' '.join(result)

sentence = "Asseses the case with careful integration and combination"
print(f"Sentence: {sentence}")
print(f"Stemmed: {stem(sentence)}")