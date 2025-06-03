def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()
  
def num_of_words(text):
  words = text.split()
  return len(words)
  
def main():
  entire_book = get_book_text("books/frankenstein.txt")
  print(entire_book)
  num_words = num_of_words(entire_book)
  print(f"{num_words} words found in the document")
  
main()

# print(get_book_text("books/frankenstein.txt"))