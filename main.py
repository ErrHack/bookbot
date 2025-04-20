def get_book_text(file_path):
  file_contents = ""
  with open(file_path) as book:
    file_contents = book.read()
  return file_contents

def count_words(book_text = "book_text"):
  book_words = book_text.split()
  return len(book_words)


def main():
  num_words = count_words(get_book_text("./books/frankenstein.txt"))
  print(f"{num_words} words found in the document")

main()
