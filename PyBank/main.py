import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
months=0
#profits and losses
pnl = 0
averagechange = 0

previous = 0
greatestIncrease = ["",0]
greatestDecrease = ["",0]


with open(csvpath,newline='', encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #months = len(csvreader)
    next(csvreader)
    change = 0
    firstline = next(csvreader)
    months = months + 1
    pnl = pnl + float(firstline[1])
    previous = float(firstline[1])
    for line in csvreader:
        amount = float(line[1])
        months = months + 1
        pnl = pnl + amount
        change = amount - previous
        if(change > greatestIncrease[1]):
            greatestIncrease = [line[0],change]
        elif(change < greatestDecrease[1]):
            greatestDecrease = [line[0],change]
        averagechange = averagechange + change
        previous = amount




        
averagechange = round(averagechange / (months - 1),2)
string =f"Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${pnl}\nAverage  Change: ${averagechange}\nGreatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})\nGreatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})"

print(string)
output_path = os.path.join("Analysis", "Analysis.txt")

with open(output_path, 'w') as text:
    text.write(string)