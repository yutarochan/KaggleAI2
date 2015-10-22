import re
import fileUtil
from nltk.corpus import words
from nltk.tokenize import RegexpTokenizer

_digits = re.compile('\d')

# Add Unique Elements to List
def addToList(self, str_to_add):
    if str_to_add not in self:
        self.append(str_to_add)

# Check String Contains Digits
def contains_digits(d):
    return bool(_digits.search(d))

# Import Dataset
dataset = fileUtil.parseTrainingSet('data/training_set.tsv')

# NLTK Load Libraries
tokenizer = RegexpTokenizer(r'\w+')

corpus = []

# Generate
for data in dataset:
    q_token = tokenizer.tokenize(data.question)
    for token in q_token:
        token = token.lower()
        token = token.replace("_", "")
        if not contains_digits(token) and not len(token) == 1:
            addToList(corpus, token)

print corpus
