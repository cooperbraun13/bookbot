import sys
from stats import (
  num_of_words, 
  char_freq,
  chars_dict_to_sorted_list,
)

# reads text of a file into a string
def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book_path = sys.argv[1]
  entire_book = get_book_text(book_path)
  num_words = num_of_words(entire_book)
  character_freq = char_freq(entire_book)
  char_sorted_list = chars_dict_to_sorted_list(character_freq)
  print_report(book_path, num_words, char_sorted_list)
  
def print_report(book_path, num_words, char_sorted_list):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("------------ Word Count ---------")
  print(f"Found {num_words} total words")
  print("------------ Character Count ----")
  for item in char_sorted_list:
    if not item["char"].isalpha():
      continue
    print(f"{item['char']}: {item['num']}")
  print("============ END ================")
  
  
main()