from nltk.util import ngrams
from nltk.tokenize import word_tokenize
 
# Sample ASIN titles
asin_titles = [
    "Do Not Give Me A Cigarette Under Any Circumstances",
    "This is a Scam dude",
]

# Tokenize and create trigrams for each title
trigrams = []

print("==============")

for title in asin_titles:
    tokens = word_tokenize(title)
    trigrams.extend(list(ngrams(tokens, 3, pad_left=0, pad_right=0)))
    print(title)
    print("==============")
    for tri in trigrams:
        print("".join(str(tri)))
    trigrams = []
    print("==============")

    def normalize(x):
        return (x - min(x)) / (max(x) - min(x))

    print(normalize(23))


