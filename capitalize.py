word = input("Please enter a string")
full_string = []
len_word = len(word)

def capitalize (word):
  idx = 0
  while idx < len_word:
    if idx == 0:
      full_string.append(word[idx].upper())
    elif word[idx] == " ":
      full_string.append(" " + word[idx+1].upper())
      idx = idx + 1
    else:
      full_string.append(word[idx])
    idx= idx + 1
  return("".join(full_string))

print(capitalize(word))
