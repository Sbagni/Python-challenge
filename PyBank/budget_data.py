
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('.','Resources','budget_data.csv')
with open(budget_csv, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)
	previous_row = next(csvreader)
 	#list to hold average change   
        change = []
        months = [] 
        total_m = 0
    
        for row in csvreader:

		net_total += row[1]
        change.append {(row[1]-previous_row[1])}
		months.append.{str(row[0])}
		total_m = total_m+1
		
	        previous_row = row

    print(profit_loss_change)
    print(net_total)
	
	avg_change = pofit_loss_change/total_m
	print(avg_change)

			
print("Financial Analysis")

print("--------------------------")

print(f"Total Months:{str(total_m)}")

print(f"Total:{int(net_total)}")

print(f"Average_change : {int(avg_change)}")



       



