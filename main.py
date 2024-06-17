import os
import csv
import statistics

csvpath = os.path.join("..","Pybank","Resources","budget_data.csv")
text_path = "Final_Analysis.txt"
outfile = os.path.join('analysis', text_path)

with open(csvpath, encoding ='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    totalmonths = []
    profits = []
    pc = []

    for row in csv_reader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))
for i in range(len(profits) - 1):
        pc.append(profits[i+1] - profits[i])
total_months = len(totalmonths)
sum_profits = sum(profits)
avg_change = (sum(pc) / len(pc))
greatest_increase = ((totalmonths[pc.index(max(pc))+1]))
greatest_decrease = ((totalmonths[pc.index(min(pc))+1]))
g_increase = max(pc)
g_decrease = min(pc)
output =print(
        f"Financial Analysis\n"
        f"---------------------\n"
        f'Total MOnths: {total_months}\n'
        f'Total Profits: {sum_profits}\n'
        f'Average Revenue Change : {avg_change}\n'
        f'Greatest Increase in Profits: {greatest_increase} {g_increase}\n'
        f'Greatest Decrease in Profits: {greatest_decrease} {g_decrease}\n'
)
