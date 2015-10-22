# AI2 - ConceptNet Prototype
# Attempt to utilizing the ConceptNet API for solving quesitons.
# Demonstration with only one question, change constant number param to change question.

import fileUtil
import prelimAnalysis as prenlp
from conceptnet5_client.web.api import Association
from conceptnet5_client.utils.result import Result

# Question Number Parameter - Specify exact element from training dataset.
QUES_NUM = 0

# Import Dataset
train = fileUtil.parseTrainingSet('data/training_set.tsv')
q = train[QUES_NUM]

# Perform NLP Preprocessing
ques = prenlp.preprocess(q.question)
ans_a = prenlp.preprocess(q.a)
ans_b = prenlp.preprocess(q.b)
ans_c = prenlp.preprocess(q.c)
ans_d = prenlp.preprocess(q.d)


print "[Question]: " + str(ques) + "\n"
print "[Answer Choices]"
print "A: " + str(ans_a)
print "B: " + str(ans_b)
print "C: " + str(ans_c)
print "D: " + str(ans_d)
print

print "[Correct Answer]: " + str(q.ans) + "\n"

# Perform Semantic Association Search on Question
a = Association()
data = a.get_similar_concepts_by_term_list(ques)
r = Result(data)

# Obtain Associtative Edges
r.parse_all_edges()
print

# Perform an Exhaustive Entity Frequency Search
# Check to see which one contains the most amount of relevant entities.

#print "[Predicted Answer]: "
#print "[Correct Answer]: " + str(q.ans) + "\n"
