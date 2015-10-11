import nltk
import fileUtil

ques = fileUtil.parseTrainingSet('data/training_set.tsv')

token = nltk.word_tokenize(ques[0].question)
print token
