import os
import csv

candidates = {}

# Path to collect data from the Resources folder
budget_csv = os.path.join('.','Resources','election_data.csv')
with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1

        total_votes = sum(candidates.values())
        total_votes

        list_candidates = candidates.keys()
        list_candidates
        votes_per = [f'{(x/total_votes)*100:.3f}%' for x in candidates.values()]
        votes_per
        winner = list(candidates.keys())[candidates.values()(max(candidates.values()))]
        winner


print("Election results")

print("--------------------------")

print(f"Total votes: {int(total_votes)}")

print("-----------------------------")

print(f'{candidates[list_candidates]}":"{candidates[votes_per]}"("{candidates[candidates.values()]}'")")

print("-------------------------------")

print(f'Winner: {str(winner)}')






