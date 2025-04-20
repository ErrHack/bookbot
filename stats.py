def count_words(book_text = "book_text"):
  book_words = book_text.split()
  return len(book_words)

def count_chars(book_text = "book_text"):
  char_counts = dict()
  for letter in book_text:
    char = letter.lower()
    if char in char_counts:
      char_counts[char] += 1
    elif char == '\n':
      pass
    else:
      char_counts[char] = 1
  return char_counts