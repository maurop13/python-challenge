import csv
from decimal import Decimal


numberMonths = 0
months = []
netAmount = 0
totalMonthlyChanges = 0
averageChange = 0
amounts=[]
change =[]
maxchange=0
minchange=0
greatestIncrease = 0
monthGreatestIncrease = "None"
greatestDecrease = 0
monthGreatestDecrease= "None"

main_Data = "C:/Users/noneo/OneDrive/Escritorio/Bootcamp/GITLABUCBER201809DATA2/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"
with open(main_Data, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    for row in csvreader:
        months.append(row[0])
        amounts.append(float(row[1]))
        netAmount = netAmount + int(row[1])
        numberMonths = len(months)
        greatestIncrease = max(amounts)
        greatestDecrease = min(amounts)
    
         
    # monthGreatestIncrease = csvreader.index(averageChange)
    for i in range(len(amounts)):
        if(i+1==len(amounts)):
            break
        else:
            change.append(amounts[i+1] - amounts[i])
    totalMonthlyChanges = sum(change)
    averageChange = totalMonthlyChanges / (numberMonths-1)
    maxchange = max(change)
    minchange = min(change)
    monthGreatestIncrease= months[change.index(maxchange)+1]
    monthGreatestDecrease = months[change.index(minchange)+1]
    
print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(numberMonths))
print("Total: $" + str(netAmount))
print("Average Change: $" + str(round(Decimal(averageChange),2)))
print("Greatest Increase in Profits: " + monthGreatestIncrease + " ($" + str (round(Decimal(maxchange),0))+")")
print("Greatest Decrease in Profits: " + monthGreatestDecrease + " ($" + str(round(Decimal(minchange),0))+")")

f = open("Bank_results.txt","w")
f.write("Financial Analysis \n ---------------------\n Total Months: " 
              + str(numberMonths)+"\n Total: $" 
              + str(netAmount)+"\n Average Change: $" 
              + str(round(Decimal(averageChange),2))
              +"\n Greatest Increase in Profits: " 
              + monthGreatestIncrease 
              + " ($" 
              + str (round(Decimal(maxchange),0))
              +")"
              +"\n Greatest Decrease in Profits: " 
              + monthGreatestDecrease 
              + " ($" 
              + str(round(Decimal(minchange),0))
              +")"
              )
f.close()
