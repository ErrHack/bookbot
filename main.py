from stats import *
import sys as s

def get_book_text(file_path):
  try:
    file_contents = ""
    with open(file_path) as book:
      file_contents = book.read()
    return file_contents
  except FileNotFoundError:
    print(f"{file_path} does not exist")
    s.exit(1)

def print_sorted_counts(file_path = "", num_words = 0, num_chars_dict_list = [{}]):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for entry in num_chars_dict_list:
    char = entry['char']
    count = entry['count']
    if char.isalpha():
      print(f"{char}: {count}")
  print("============= END ===============")
  

def main():
  if len(s.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    s.exit(1)
  file_path = s.argv[1]
  print_sorted_counts(file_path,
                      count_words(get_book_text(file_path)),
                      sort_char_counts(count_chars(get_book_text(file_path)))
                     )


main()

