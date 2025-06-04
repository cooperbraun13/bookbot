# counts the number of words in the text
def num_of_words(text):
  words = text.split()
  return len(words)

# counts the number of times each character appears in the text
def char_freq(text):
  freq = {}
  lowercase_text = text.lower()
  for char in lowercase_text:
    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
  return freq

def sort_on(dict):
  return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
  sorted_list = []
  for char in num_chars_dict:
    sorted_list.append({"char": char, "num": num_chars_dict[char]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list