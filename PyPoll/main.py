import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
count = 0
candidates = []
votes = []
with open(csvpath,newline='',encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        count = count + 1
        inlist = False
        for i in range(len(candidates)):
            if(row[2] == candidates[i]):
                votes[i] = votes[i] + 1
                inlist = True
                break
        if(not inlist):
            candidates.append(row[2])
            votes.append(1)

text = "Election Results\n"
text = text+"-------------------------\n"
text = text+ f"Total Votes: {count}\n"
text = text+"-------------------------\n"
winner = 0
for i in range(len(candidates)):
    text = text+f"{candidates[i]}: {round((votes[i]/count)*100,2)}% ({votes[i]})\n"
    if(votes[i] > votes[winner]):
        winner = i
text = text+"-------------------------\n"
text = text+f"Winner: {candidates[winner]}\n"
text = text+"-------------------------\n"

print(text)
output_path = os.path.join("Analysis", "Analysis.txt")

with open(output_path, 'w') as output:
    output.write(text)

