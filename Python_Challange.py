import os
import csv

csvpath = os.path.join("Resources","Budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    for row in csvreader:

# The total number of months included in the dataset

    header=next("budget_data.csv)
    Total_Number_of_Months = [0]
        for r in csvreader:
            Total_Number_of_Months += 1
            print(Total_Number_of_Months)

# The net total amount of "Profit/Losses" over the entire period

Total_PrandL = []

# The changes in "Profit/Losses" over the entire period, and then the average of those changes



# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period
