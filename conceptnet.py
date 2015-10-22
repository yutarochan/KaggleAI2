# -*- coding: utf-8 -*-

# Kaggle AI2 - ConceptNet5 Model
# Implementation of the conceptnet5 for AI2 Q&A system.
# This program is a demonstaiton for one question only.

import random
import fileUtil
import prelimAnalysis as prenlp
from conceptnet5_client.web.api import Association
from conceptnet5_client.utils.result import Result

def computeScore(sim, ans):
    pts = 0
    for a in ans:
        for s in sim:
            if a in s[0].encode('utf-8'):
                pts += s[1]
    return float(pts) / len(sim)

# Training set paramter - change accordinly to select specific trianing example

# Import Dataset
data = fileUtil.parseTrainingSet('data/training_set.tsv')

correct = 0

for idx in range(0, len(data)):
    q = data[idx]

    # Perform NLP Preprocessing
    ques = prenlp.preprocess(q.question)
    ans_a = prenlp.preprocess(q.a)
    ans_b = prenlp.preprocess(q.b)
    ans_c = prenlp.preprocess(q.c)
    ans_d = prenlp.preprocess(q.d)

    print "Question: " + str(q.question)
    print "A: " + str(q.a)
    print "B: " + str(q.b)
    print "C: " + str(q.c)
    print "D: " + str(q.d)

    # Generate Semantic Graph from Question
    a = Association(filter="/c/en", limit=30)
    semnet = a.get_similar_concepts_by_term_list(ques)
    r = Result(semnet)

    # Parse Similarity
    similar = r.get_similar()

    if len(similar) > 0:
        # Splice Leading API Directory
        for word in similar:
            word[0] = word[0][6:]

        print "\n"
        print similar
        print "\n"

        # Compute Score Probabilities
        prob = [str(computeScore(similar, ans_a)),
                str(computeScore(similar, ans_b)),
                str(computeScore(similar, ans_c)),
                str(computeScore(similar, ans_d))]

        print "<SCORE PROBABILITIES>"
        print prob

        prob = map(float, prob)

        if sum(prob) == 0:
            chidx = random.randint(0,3)
        else:
            # Obtain Letter Choice
            chidx = prob.index(max(prob))
    else:
        chidx = random.randint(0,3)

    guess = {0: "A", 1: "B", 2: "C", 3: "D"}
    print "GUESS: " + str(guess[chidx])
    print "ANSWER: " + str(q.ans)

    if guess[chidx] == str(q.ans):
        print "correct"
        correct += 1

# print "Total Score: " + str(float(correct)/len(data))
