def count_words(book_text = "book_text"):
  book_words = book_text.split()
  return len(book_words)

def count_chars(book_text = "book_text"):
  char_counts = dict()
  for letter in book_text:
    char = letter.lower()
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts

def sort_on(char_dict = {}):
  return char_dict["count"]

def sort_char_counts(char_counts = {}):
  char_count_list = []
  for char in char_counts:
    char_count_list.append({"char": char, "count": char_counts[char]})
    char_count_list.sort(reverse=True, key=sort_on)
  return char_count_list