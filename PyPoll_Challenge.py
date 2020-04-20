# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# Create a filename variable to a direct path to the file
file_to_save = 'analysis/election_analysis.txt'

# 1. Initialize a total vote counter.
total_votes = 0

# County options and county votes
county_options = []
votes_by_county = {}
county_votes = 0
county_name = ""
largest_turnout = ""


# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        total_votes += 1
        #Print County name from each row
        county_name = row[1]
        #Add the county name to the county list
        if county_name not in county_options:
            county_options.append(county_name)
            #track county votes
            votes_by_county[county_name] = 0
        votes_by_county[county_name] += 1

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

#Save results to the text file
with open (file_to_save, "w") as txt_file:
#Print the final cote vount to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:  {total_votes:,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    #Save the final count to the text file.
    txt_file.write(election_results)

    for county in votes_by_county:
        # Retrieve vote count and percentage.
        votes = votes_by_county[county]
        #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        # save the cadidate results to txt file
        txt_file.write(county_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            largest_turnout = county

        county_results = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_turnout}\n"
            f"-------------------------\n")    
        # print each candidate's voter count and percentage to terminal
        print(county_results)
        # save the cadidate results to txt file
        txt_file.write(county_results)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        #3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    
        # print each candidate's voter count and percentage to terminal
        print(candidate_results)
        # save the cadidate results to txt file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate
    #4. Print the candidate name and percentage of votes to terminal.
        winning_candidate_summary = (
            f"-----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)
