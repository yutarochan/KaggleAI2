# Kaggle - The Allen AI Science Challenge
import re
import csv

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

# Parse Training Set Data
def parseTrainingSet(path):
    questions = []

    # Read Training Dataset
    file = open(path, 'r')
    file.readline() # Skip File Header

    # Parse Dataset
    for data in file:
       r = re.split(r'\t+', data)
       q = Question(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
       questions.append(q)

    return questions

# Output CSV File
def outputCSV(data, file_out):
    with open(file_out, 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='\t')
        csvwriter.writerow(["id,correctAnswer"])
        for rowdata in data:
            csvwriter.writerow([str(rowdata[0]) + "," + rowdata[1]])

# Unit Testing
if __name__ == "__main__":
    # Read Dataset Input
    dataset = parseTrainingSet('data/training_set.tsv')
    print len(dataset)

    # CSV Output
    test_data = [[1, 'A'], [2, 'B'], [3, 'C']]
    outputCSV(test_data, "test.csv")
