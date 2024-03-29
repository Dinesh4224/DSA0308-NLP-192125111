from nltk.corpus import wordnet
from nltk.wsd import lesk
import nltk

# Get input from user
word = input("Enter a word: ")
sentence = input("Enter a sentence containing the word: ")

# Perform word sense disambiguation
sense = lesk(sentence.split(), word)

# Print the disambiguated sense
if sense:
    print("Disambiguated sense:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found for the word in the given context.")
