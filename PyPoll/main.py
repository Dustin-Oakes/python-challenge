##### PyPoll #####
# PyPoll Instructions
#
# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#
# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns:
# "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:
#
#  - The total number of votes cast
#
#  - A complete list of candidates who received votes
#
#  - The percentage of votes each candidate won
#
#  - The total number of votes each candidate won
#
#  - The winner of the election based on popular vote.
#
# Your analysis should look similar to the following:
#
#
#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 369711
#  -------------------------
#  Charles Casper Stockham: 23.049% (85213)
#  Diana DeGette: 73.812% (272892)
#  Raymon Anthony Doane: 3.139% (11606)
#  -------------------------
#  Winner: Diana DeGette
#  -------------------------
#  ```
#
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#
###########

#Imports and Variable initialization
import os, csv
voteCount = 0
candidateNames = []
voteList = []
winningNumVotes = 0
winningCandidate = "none"
currentCandidateTotalVotes = 0
csvPath = './Resources/election_data.csv'


#Loop based on PyBank activity - Load file as a CSV object
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #For each row in the CSV object, check for new candidateNames and add the vote to the voteList
    for currentRow in csvReader:
        
        #If checking the header row, use a null task to skip
        if voteCount == 0:
            print()
        else:

            #Add candidate to candidateNames if they are not already on the list
            if candidateNames.count(currentRow[1]) < 1:
                candidateNames.append(currentRow[1])

            #Add the candidate name to the voteList, even if it's already there
            voteList.append(currentRow[1])

        #Every loop should iterate voteCount
        voteCount += 1

#After the loop, adjust voteCount to account for the header row
voteCount -= 1


#Start printing results
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(voteCount))
print('-------------------------')

#For each Candidate
for i in candidateNames:
    
    #Use a variable so we don't have to keep counting
    currentCandidateTotalVotes = voteList.count(i)

    #Check if the candidtate has the highest count so far, record them as the winner if so
    if winningNumVotes < currentCandidateTotalVotes:
        winningNumVotes = currentCandidateTotalVotes
        winningCandidate = i

    #Print candidate results
    print(i + ': ' +  str(round(100 * currentCandidateTotalVotes / voteCount , 3)) + '% (' + str(currentCandidateTotalVotes) + ')')

#print winner
print('-------------------------')
print('Winner: ' + winningCandidate)
print('-------------------------')


#Export results to a text file
with open('./analysis/Results.txt', 'w') as txtResults:
    txtResults.write('Election Results')
    txtResults.write('\n')
    txtResults.write('-------------------------')
    txtResults.write('\n')
    txtResults.write('Total Votes: ' + str(voteCount))
    txtResults.write('\n')
    txtResults.write('-------------------------')
    txtResults.write('\n')

    #For each Candidate
    for i in candidateNames:
        #Write candidate results (winner already determined)
        txtResults.write(i + ': ' +  str(round(100 * currentCandidateTotalVotes / voteCount , 3)) + '% (' + str(currentCandidateTotalVotes) + ')')
        txtResults.write('\n')

    txtResults.write('-------------------------')
    txtResults.write('\n')
    txtResults.write('Winner: ' + winningCandidate)
    txtResults.write('\n')
    txtResults.write('-------------------------')