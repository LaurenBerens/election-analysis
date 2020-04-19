# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# Create a filename variable to a direct path to the file
file_to_save = 'analysis/election_analysis.txt'

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning candidate and willing count tracker variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add the total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #3 Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
with open (file_to_save, "w") as txt_file:
#Print the final cote vount to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:  {total_votes:,}\n"
        f"-------------------------\n")
print(election_results, end="")
#Save the final count to the text file.
txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    #1. Iterate through the cadidate list.
for candidate in candidate_votes:
    #2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    #3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
    #AAAAAprint(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    #1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning percent =
        #vote percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate
    #4. Print the candidate name and percentatge of votes.
winning_candidate_summary = (
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n")
#AAAAAAprint(winning_candidate_summary)





