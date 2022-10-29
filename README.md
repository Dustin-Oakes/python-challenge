# python-challenge

PyBank and PyPoll

Both the PyBank and PyPoll folders have:
 - a main file, which contains the complete program per the challenge instructions
 - a Jupyter notebook which was used as a working copy during program writing
    --the Jupyter notebook has less #notes than the main file as well
 - a Resources folder containing the CSVs included from the challenge instructions
 - an analysis folder containing the results of the program in a txt file



Below is a copy of the instructions, which are also written in each file

# PyBank Instructions

 In this challenge, you are tasked with creating a Python script to analyze the financial records of your company.
 You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
 The dataset is composed of two columns: "Date" and "Profit/Losses". (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

 Your task is to create a Python script that analyzes the records to calculate each of the following:

  - The total number of months included in the dataset

  - The net total amount of "Profit/Losses" over the entire period

  - The changes in "Profit/Losses" over the entire period, and then the average of those changes

  - The greatest increase in profits (date and amount) over the entire period

  - The greatest decrease in profits (date and amount) over the entire period

 Your analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```

 In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# PyPoll Instructions

 In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

 You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns:
 "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following:

  - The total number of votes cast

  - A complete list of candidates who received votes

  - The percentage of votes each candidate won

  - The total number of votes each candidate won

  - The winner of the election based on popular vote.

 Your analysis should look similar to the following:


  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```

 In addition, your final script should both print the analysis to the terminal and export a text file with the results.
