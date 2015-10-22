import nltk
import fileUtil
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

# Initially Load to Save Procesing Time
tokenizer = RegexpTokenizer(r'\w+')
stops = stopwords.words('english')
stemmer = SnowballStemmer("english")

def preprocess(text):
    # Tokenize and Remove Punctuation (Using regex tokenizer)
    token = tokenizer.tokenize(text)

    # Stop Word Removal
    word_list = token[:]
    filtered_word_list = word_list[:] #make a copy of the word_list
    for word in word_list: # iterate over word_list
      if word in stops:
        filtered_word_list.remove(word)

    # Stemming Variation 1: Porter Stemmer
    # stemmer = PorterStemmer()
    # stemmed = [stemmer.stem(plural) for plural in filtered_word_list]
    # print stemmed

    # Stemming Variation 2: Snowball Stemmer
    # stemmed = [stemmer.stem(plural) for plural in filtered_word_list]

    return filtered_word_list

# Unit Testing
if __name__ == "__main__":
    ques = fileUtil.parseTrainingSet('data/training_set.tsv')

    # Testing with just sample data...
    print preprocess(ques[0].question)
    print preprocess(ques[1].question)
    print preprocess(ques[2].question)
