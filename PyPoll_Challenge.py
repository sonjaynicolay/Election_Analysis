# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter 
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# County Options and County votes.
county_options = []
county_votes = {}

# Track Winning Candidate Vote count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Winning county, count and percentage.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header
    headers = next(file_reader)
   
    # Print each row in the CSV file
    for row in file_reader:

        # Initialize a total vote counter.
        #Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row..
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Begin tracking candidates vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        #If county does not match any existing county in the county list
        if county_name not in county_options:
            county_options.append(county_name)
            # Begin tracking candidates vote count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results) 

    for county_name in county_votes:
        # Retrieve vote count of a candidate
        votes_county = county_votes.get(county_name)
        # Retrieve vote percentage
        county_percentage = float(votes_county) / float(total_votes) * 100
        # Print each candidate's name, vote count, and percentage of the
        # the votes to the terminal.
        county_result=(f"{county_name}: {county_percentage:.1f}% ({votes_county:,})\n")
        print(county_result)
        # Save County Results to txt file
        txt_file.write(county_result)

        
        # Determine winning county, county winning percentage.
        if (votes_county > winning_county_count) and (county_percentage > winning_county_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_county_count = votes_county
            winning_county = county_name
            winning_county_percentage = county_percentage
    
    # Winning County Summary    
    winning_county_summary = (
        f"------------------------\n"
        f" Largest County Turnout : {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)  


    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Retrieve vote percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate's name, vote count, and percentage of the
        # the votes to the terminal.
        candidate_result=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_result)
        # Save Candidate Results to txt file
        txt_file.write(candidate_result)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    
    # Winning Candidate Summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary, end="")
    txt_file.write(winning_candidate_summary)


   





