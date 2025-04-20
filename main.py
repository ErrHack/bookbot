from stats import *

def get_book_text(file_path):
  file_contents = ""
  with open(file_path) as book:
    file_contents = book.read()
  return file_contents

def main():
  book_text = get_book_text("./books/frankenstein.txt")
  num_words = count_words(book_text)
  print(f"{num_words} words found in the document")
  num_chars = count_chars(book_text)
  for char in num_chars:
    print(f"\'{char}\': {num_chars[char]}")

main()
