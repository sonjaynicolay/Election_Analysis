#Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)

    total_votes = 0
    #Candidate Options and Candidate Votes.
    candidate_options = []
    candidate_votes = {}
    
    #Print each row in the CSV file
    for row in file_reader:

        #Initialize a total vote counter.
        #Add to the total vote count.
        total_votes += 1
        candidate = row[2]
        print(candidate)
        print(candidate not in candidate_options)
        # Add candidate to options if not in options already
        if candidate not in candidate_options:
            candidate_options.append(candidate)
            print(candidate_options)
            # break
            #Begin tracking candidates vote count.
            candidate_votes[candidate] = 1
        else: 
        #Add a vote to the candidate's count.
            candidate_votes[candidate] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Retrieve vote percentage
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate's name, vote count, and percentage of the
    # the votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

#Winning Candidate Summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary, end="")


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
   
    # Save the final vote count to the text file.
    txt_file.write(election_results)
   
    #Step 1 Initialize a County List and a Dictionary that will hold votes
    county_list = []
    county_votes = {}
    for row in file_reader:
        
        total_votes +- 1
        county_name = row[1]

        # Print the county vote dictionary
        print(county_votes.__dict__, end="")
        txt_file.write(election_results)


        print (top_county_turnout, end="")

        
        county_list.append(county_name)
        county_list(county_name)



#Initialize a variable that will hold number of votes of the county
# that had the largest turnout
top_county_count = 0
