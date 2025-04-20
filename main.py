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
  num_chars_dict_list = sort_char_counts(num_chars)
  for dict_entry in num_chars_dict_list:
    print(dict_entry)

main()
