from stats import num_of_words

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
def main():
  entire_book = get_book_text("books/frankenstein.txt")
  print(entire_book)
  num_words = num_of_words(entire_book)
  print(f"{num_words} words found in the document")
  
main()