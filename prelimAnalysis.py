import nltk
import fileUtil
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

# Just a quick test of some of NLTK's functionality.

ques = fileUtil.parseTrainingSet('data/training_set.tsv')

# Tokenize and Remove Punctuation (Using regex tokenizer)
tokenizer = RegexpTokenizer(r'\w+')
token = tokenizer.tokenize(ques[0].question)

# Stop Word Removal
word_list = token[:]
stops = stopwords.words('english')
filtered_word_list = word_list[:] #make a copy of the word_list
for word in word_list: # iterate over word_list
  if word in stops:
    filtered_word_list.remove(word)

# Stemming Variation 1: Porter Stemmer
# stemmer = PorterStemmer()
# stemmed = [stemmer.stem(plural) for plural in filtered_word_list]
# print stemmed

# Stemming Variation 2: Snowball Stemmer
stemmer = SnowballStemmer("english")
stemmed = [stemmer.stem(plural) for plural in filtered_word_list]
print stemmed
