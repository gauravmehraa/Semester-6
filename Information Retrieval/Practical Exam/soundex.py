def soundex(s):
  s = s.upper()
  result = [s[0]] # keep first letter as it is
  mapping = {
    ('A', 'E', 'I', 'O', 'U', 'H', 'W', 'Y'): '0',
    ('B', 'F', 'P', 'V'): '1',
    ('C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'): '2',
    ('D', 'T'): '3',
    ('L',): '4',
    ('M', 'N'): '5',
    ('R',): '6',
  }

  encoded = []
  for char in s[1:]: # skip first letter
    for key in mapping:
      if char in key:
        encoded.append(mapping[key])
        break

  filtered = []
  for i in range(len(encoded)):
    if i == 0 or encoded[i] != encoded[i - 1]: # skip duplicates
      filtered.append(encoded[i])

  result += [char for char in filtered if char != '0'] # remove zeroes
  while len(result) < 4: result.append('0') # pad to 4
  return ''.join(result[:4]) # return first 4
    
words = ["HERMAN", "HERMANN", "ASHCROFT", "ASHCRAFT", "PFISTER", "UNDERSTANDING"]
for s in words:
  print(f"{s}: {soundex(s)}")