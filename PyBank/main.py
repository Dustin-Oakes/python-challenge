##### PyBank #####
# PyBank Instructions
#
# In this challenge, you are tasked with creating a Python script to analyze the financial records of your company.
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
# The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)
#
# Your task is to create a Python script that analyzes the records to calculate each of the following:
#
#  - The total number of months included in the dataset
#
#  - The net total amount of "Profit/Losses" over the entire period
#
#  - The changes in "Profit/Losses" over the entire period, and then the average of those changes
#
#  - The greatest increase in profits (date and amount) over the entire period
#
#  - The greatest decrease in profits (date and amount) over the entire period
#
# Your analysis should look similar to the following:
#
#  ```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $22564198
#  Average Change: $-8311.11
#  Greatest Increase in Profits: Aug-16 ($1862002)
#  Greatest Decrease in Profits: Feb-14 ($-1825558)
#  ```
#
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#
###########

#Imports and Variable initialization
import os, csv
monthCount = 0
totalChange = 0
greatestIncrease = 0
greatestIncreaseDate = "None"
greatestDecrease = 0
greatestDecreaseDate = "None"
csvPath = './Resources/budget_data.csv'


#Load file as a CSV object
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #For each row in the CSV object, add to totals and check for new max/min
    for currentRow in csvReader:
        
        #If checking the header row, use a null task to skip
        if monthCount == 0:
            print()
        else:

            totalChange = totalChange + int(currentRow[1])

            if int(currentRow[1]) > int(greatestIncrease):
                greatestIncrease = currentRow[1]
                greatestIncreaseDate = currentRow[0]

            if int(currentRow[1]) < int(greatestDecrease):
                greatestDecrease = currentRow[1]
                greatestDecreaseDate = currentRow[0]

        #Every loop in for should iterate monthCount, which is currently used as the line count
        monthCount += 1


#After the loop, adjust monthCount to account for the header row
monthCount -= 1


#Export results to a text file
with open('./analysis/Results.txt', 'w') as txtResults:
    txtResults.write('Financial Analysis')
    txtResults.write('\n')
    txtResults.write('----------------------------')
    txtResults.write('\n')
    txtResults.write('Total Months: ' + str(monthCount))
    txtResults.write('\n')
    txtResults.write('Total: $' + str(totalChange))
    txtResults.write('\n')
    txtResults.write('Average Change: $' + str(round(totalChange / monthCount,2)))
    txtResults.write('\n')
    txtResults.write('Greatest Increase in Profits: ' + greatestIncreaseDate + ' ($' + str(greatestIncrease) + ')')
    txtResults.write('\n')
    txtResults.write('Greatest Decrease in Profits: ' + greatestDecreaseDate + ' ($' + str(greatestDecrease) + ')')


#Write results to terminal
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(monthCount))
print('Total: $' + str(totalChange))
print('Average Change: $' + str(round(totalChange / monthCount,2)))
print('Greatest Increase in Profits: ' + greatestIncreaseDate + ' ($' + str(greatestIncrease) + ')')
print('Greatest Decrease in Profits: ' + greatestDecreaseDate + ' ($' + str(greatestDecrease) + ')')