def removal(text):
  stop_words = {
  "a", "an", "the", "is", "in", "at", "of", "on", "and", "or", "to", "it", "this", "that", "from", "with",
  "as", "for", "by", "was", "were", "be", "been", "are", "but", "not", "so", "if", "then", "when", "all",
  "can", "will", "would", "should", "could", "has", "have", "had", "you", "your", "we", "our", "they",
  "their", "he", "she", "him", "her", "i", "me", "my", "us", "what", "which", "who", "whom", "where",
  "why", "how"
  }
  text = ''.join(char for char in text if char.isalnum() or char.isspace())
  words = text.lower().split()
  filtered = [word for word in words if word not in stop_words]
  return ' '.join(filtered)

# wikipedia text
original = '''Information retrieval (IR) in computing and information science is the task of identifying and retrieving information system resources that are relevant to an information need. The information need can be specified in the form of a search query. In the case of document retrieval, queries can be based on full-text or other content-based indexing. Information retrieval is the science of searching for information in a document, searching for documents themselves, and also searching for the metadata that describes data, and for databases of texts, images or sounds.'''
print("Original Text:")
print(original)

processed = removal(original)
print("\nProcessed Text:")
print(processed)
