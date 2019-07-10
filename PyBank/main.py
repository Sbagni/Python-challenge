
import os
import csv


greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]   
change_list = []
total_change = 0
months = [] 
total_m = 0
net_total=0


budget_csv = os.path.join('.','Resources','budget_data.csv')
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    previous_row = next(csvreader)
    for row in csvreader:

        net_total+=int(row[1])
        total_m=total_m+1
        change_value = int(row[1]-previous_row[1])

        change_list.append(change_value)
        months.append (row[0])
        previous_row = row

        total_change = total_change + change_value 
        if change_value > greatest_increase[1]:
           greatest_increase[0] = str(row[0])
           greatest_increase[1] = change_value

        if netchange < greatest_decrease[1]:
           greatest_decrease[0] = str(row[0])
           greatest_decrease[1] = change_value
		
    
    print (total_change)
    print(net_total)
    print (total_m)
    avg_change = total_change/len(months)
    print(avg_change)
        
	   
print("Financial Analysis")

print("--------------------------")

print(f"Total Months:{str(total_m)}")

print(f"Total:{int(net_total)}")

print(f"Average_change : {int(avg_change)}")

print(f"Greatest Increase in profit:{ greatest_increase('[' str(row) ']') + change_value}")

print(f"Greatest Decrease in profit:{ greatest_decrease('[' str(row) ']') + change_value}")











       



