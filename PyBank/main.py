import os
import csv
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    months = 0
    total = 0
    change = 0
    previous_revenue = 0
    max_profit= 0
    max_loss = 0
    total_change = 0
    for row in csvreader:
        # print(row)
        #make prof/loss a integer
        row[1]= int(row[1])
        # total months
        months = months + 1 
        # sum of profits and losses
        total = total + (row[1])
        #loop to find changes in profit and losses
        change = row[1] - previous_revenue
        if previous_revenue == 0:
            change= 0
        
        total_change= total_change + change
        previous_revenue = row[1]
        if(change > max_profit):
            max_profit = change
            max_profit_date = row[0]
        if(change < max_loss):
            max_loss = change
            max_loss_date = row[0] 
        avg_change = total_change / months
        avg_change = round(avg_change, 2)
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: ${max_profit} during {max_profit_date}')
print(f'Greatest Decrease in Losses: ${max_loss} during {max_loss_date}')

out_path = os.path.join("resultsbank.txt")
with open(out_path, 'w') as txtfile:
    print(f'Financial Analysis', file=txtfile)
    print(f'----------------------------', file=txtfile)
    print(f'Total Months: {months}', file=txtfile)
    print(f'Total: ${total}', file=txtfile)
    print(f'Average Change: ${avg_change}', file=txtfile)
    print(f'Greatest Increase in Profits: ${max_profit} during {max_profit_date}', file=txtfile)
    print(f'Greatest Decrease in Losses: ${max_loss} during {max_loss_date}', file=txtfile)