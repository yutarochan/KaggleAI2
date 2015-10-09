import csv
import random

with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='\t')
    spamwriter.writerow(["id,correctAnswer"])
    for i in range(102501,110633):
        spamwriter.writerow([str(i) + "," + random.choice('ABCD')])
