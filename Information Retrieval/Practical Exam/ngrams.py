def ngrams(sentence, n):
  result = []
  words = [f"${word}$" for word in sentence.split()]
  for word in words:
    for i in range(len(word) - n + 1):
      result.append(word[i:i+n])
  return result

def nwords(sentence, n):
  result = []
  words = sentence.split()
  for i in range(len(words) - n + 1):
    result.append(' '.join(words[i:i+n]))
  return result

n = 4
sentence = "war turing worked national physical laboratory designed automatic computing engine one first designs"
grams = ngrams(sentence, n)
words = nwords(sentence, n)
print(grams)