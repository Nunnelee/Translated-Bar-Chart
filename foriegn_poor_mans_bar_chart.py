""" Map Letters from string into dictionary & print bar chart of frequency."""
import translate
import sys
import pprint
from collections import defaultdict

# Changes from English to Spanish
from translate import Translator
translator= Translator(to_lang="es")


# Note: text should be a short phrase to fit in IDLE window
text = input('Type in a phrase, but keep it short: ')

translation = translator.translate(text)

ALPHABET =  'abcdefghijklmnopqrstuvwxyz'

# defaultdict module lets you build dictionary keys on the fly!
mapped = defaultdict(list)
for character in translation:
    character = character.lower()
    if character in ALPHABET:
        mapped[character].append(character)

# pprint lets you print stacked output:
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print("{}\n".format(translation), file=sys.stderr)
pprint.pprint(mapped, width=110)   

