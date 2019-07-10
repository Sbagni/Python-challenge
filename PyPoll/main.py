import os
import csv

vote_count = 0 
candidate_names = []
candidate_votes = [0,0,0,0]


# Path to collect data from the Resources folder
budget_csv = os.path.join('.','Resources','election_data.csv')
with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

        vote_count +=1
        
        	if candidate[0] =!candidate[0+1]:
    		candidate_names.append.[str(candidate)]
            print(candidate)

            

            for candidates in candidate_names:
            	candidate_votes +=1
            	print(candidate_votes)
            	next candidate
            	vote_percentage = candidate_votes/vote_count*100
            	print(vote_percentage) 
            	 
         print(vote_count)     
   

print("Election results")

print("--------------------------")

print(f"Total votes: {int(vote_count)}")

print("---------------------------")

print()




