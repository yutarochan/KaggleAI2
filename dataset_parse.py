# Kaggle - The Allen AI Science Challenge
import re

# Dataset Data Structure
class Question(object):
    def __init__(self, qid, question, ans, a, b, c, d):
        self.id = qid
        self.question = question
        self.ans = ans
        self.a = a
        self.b = b
        self.c = c
        self.d = d

questions = []

# Read Training Dataset
file = open('training_set.tsv', 'r')
file.readline() # Skip File Header

# Parse Dataset
for data in file:
   r = re.split(r'\t+', data)
   q = Question(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
   questions.append(q)

# Check to see number of datasets
# print len(questions)

    
