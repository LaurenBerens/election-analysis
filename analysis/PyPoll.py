# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of cotes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
import csv
import os
# Assign a variab;e for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file
# Create a filename variable to a direct path to the file
file_to_save = 'analysis/election_analysis.txt'
with open(file_to_load) as election_data:
    # To do: perform analysis
# Using the with statement open the file as a text file
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next(file_reader)
    print(headers)




