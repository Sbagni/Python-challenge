import os
import csv

vote_count = 0 
candidate_list = []
Candidate = str(row [0])

# Path to collect data from the Resources folder
budget_csv = os.path.join('.','Resources','election_data.csv')
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        vote_count = vote_count+1
        candidate_list.append(str(Candidate)

        	for Candidate in candidate_list
        	print(Candidate)

     print(vote_count)
   

print("Election results")

print("--------------------------")

print(f"Total votes: {int(vote_count)}")

print("---------------------------")




