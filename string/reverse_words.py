"""
We are given a string and we need to reverse words of a given string
"""
word = "The lazy dog is trying to jump a wall"
# expected out: wall a jump to trying is dog lazy The

words = word.split()[::-1]

reversed_word = []

for w in words:

  # append reverse words
  reversed_word.append(w)

# Join the split words
print(" ".join(reversed_word))


