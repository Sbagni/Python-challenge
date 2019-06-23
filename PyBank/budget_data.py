
import os
import csv

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]   
change = []
months = [] 
total_m = 0
net_total=0


# Path to collect data from the Resources folder
budget_csv = os.path.join('.','Resources','budget_data.csv')
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
	previous_row = next(csvreader)

	for row in csvreader:
       
       net_total += int (row[1])
       change.append {int(row[1]-previous_row[1])}
       netchange = {int(row[1]-previous_row[1])}
	   months.append.{str(row[0])}
	   total_m = total_m+1
       previous_row = row

		if netchange > greatest_increase[1]:
           greatest_increase[0] = str(row[0])
           greatest_increase[1] = netchange

        if netchange < greatest_decrease[1]:
           greatest_decrease[0] = str(row[0])
           greatest_decrease[1] = netchange
		
	   
    print(change)
    print(net_total)
	
	avg_change = sum(change)/total_m
	print(avg_change)

			
print("Financial Analysis")

print("--------------------------")

print(f"Total Months:{str(total_m)}")

print(f"Total:{int(net_total)}")

print(f"Average_change : {int(avg_change)}")

print(f"Greatest Increase in profit:{ "[" + str(row) "]" + greatest_increase(int(netchange))}")
print(f"Greatest Decrease in profit:{ "[" + str(row) "]" + greatest_decrease(int(netchange))}")






       



