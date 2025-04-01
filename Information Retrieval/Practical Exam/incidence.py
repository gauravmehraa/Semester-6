from nltk.corpus import stopwords

# run once to download all stopwords 
# nltk.download('stopwords')

def stopword_removal(text):
  stopwords_set = set(stopwords.words('english'))
  cleaned = ''.join(char for char in text if char.isalnum() or char.isspace())
  tokens = cleaned.lower().split()
  filtered_tokens = [token for token in tokens if token not in stopwords_set]
  return ' '.join(filtered_tokens)

def incidence_matrix(texts):
  n = len(texts)
  matrix = [] # incidence matrix
  seen = set()
  vocab = [] # collection of all terms

  for i in range(n):
    texts[i] = stopword_removal(texts[i]).split()
    for token in texts[i]:
      if token not in seen: vocab.append(token)
      seen.add(token)
  
  positions = {} # for storing the row number of a term
  for row, term in enumerate(vocab):
    frequencies = [1 if term in texts[i] else 0 for i in range(n)] # represents a row of 0/1  
    matrix.append([term] + frequencies) # [term, 0, 1, ...]
    positions[term] = row # e.g. { term: 2 }

  return matrix, positions

def search(query, matrix, positions):
  n = len(matrix[0]) - 1
  terms = query.split()[::2]
  operators = query.split()[1::2]

  rows = [] # represents rows of the queried terms
  for term in terms:
    row = positions.get(term)
    if row is None: rows.append([0] * n) # term does not exist
    else: rows.append(matrix[row][1:]) # zero index is the term

  result = rows[0] # by default
  if len(rows) == 1: return result # only 1 term in query

  for index, row in enumerate(rows[1:]):
    operator = operators[index]
    for i in range(n): #  for each term
      if operator == "AND": result[i] &= row[i]
      elif operator == "OR": result[i] |= row[i]
  return result

texts = [
  "Alan Mathison Turing (23 June 1912 to 7 June 1954) was an English mathematician, computer scientist, logician, cryptanalyst, philosopher and theoretical biologist. He was highly influential in the development of theoretical computer science, providing a formalisation of the concepts of algorithm and computation with the Turing machine, which can be considered a model of a general-purpose computer. Turing is widely considered to be the father of theoretical computer science.",
  "Born in London, Turing was raised in southern England. He graduated from King's College, Cambridge, and in 1938, earned a doctorate degree from Princeton University. During World War II, Turing worked for the Government Code and Cypher School at Bletchley Park, Britain's codebreaking centre that produced Ultra intelligence. He led Hut 8, the section responsible for German naval cryptanalysis. Turing devised techniques for speeding the breaking of German ciphers, including improvements to the pre-war Polish bomba method, an electromechanical machine that could find settings for the Enigma machine. He played a crucial role in cracking intercepted messages that enabled the Allies to defeat the Axis powers in many engagements, including the Battle of the Atlantic.",
  "After the war, Turing worked at the National Physical Laboratory, where he designed the Automatic Computing Engine, one of the first designs for a stored-program computer. In 1948, Turing joined Max Newman's Computing Machine Laboratory at the Victoria University of Manchester, where he helped develop the Manchester computers and became interested in mathematical biology. Turing wrote on the chemical basis of morphogenesis and predicted oscillating chemical reactions such as the Belousov Zhabotinsky reaction, first observed in the 1960s. Despite these accomplishments, he was never fully recognised during his lifetime because much of his work was covered by the Official Secrets Act.",
  "In 1952, Turing was prosecuted for homosexual acts. He accepted hormone treatment, a procedure commonly referred to as chemical castration, as an alternative to prison. Turing died on 7 June 1954, aged 41, from cyanide poisoning. An inquest determined his death as suicide, but the evidence is also consistent with accidental poisoning. Following a campaign in 2009, British prime minister Gordon Brown made an official public apology for 'the appalling way Turing was treated'. Queen Elizabeth II granted a pardon in 2013. The term 'Alan Turing law' is used informally to refer to a 2017 law in the UK that retroactively pardoned men cautioned or convicted under historical legislation that outlawed homosexual acts.",
  "Turing left an extensive legacy in mathematics and computing which today is recognised more widely, with statues and many things named after him, including an annual award for computing innovation. His portrait appears on the Bank of England 50 note, first released on 23 June 2021 to coincide with his birthday. The audience vote in a 2019 BBC series named Turing the greatest person of the 20th century."
]

matrix, positions = incidence_matrix(texts)
print(search("turing AND computer", matrix, positions))