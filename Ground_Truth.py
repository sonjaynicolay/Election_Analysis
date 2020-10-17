# Add our dependencies.
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

    votes = 0
    candidate_options = []
    candidate_votes = {}
    for row in file_reader:

        votes += 1
        candidate = row[2]

        # Add candidate to options if not in options already
        if candidate not in candidate_options:
            candidate_options.append(candidate)
            candidate_votes[candidate] = 0

        candidate_votes[candidate] += 1


# votes
# candidate_options
# candidate_votes​

# voting_percentages = []
# for key in candidate_votes.values():​
#     value = candidate_votes[key]

#     cand_percent =  value / votes * 100​
#     analysis_string = f"{key} got {cand_percent:.1f}% of the votes"  

#     voting_percentages.append(analysis_string)​​


# # Determine the percentage of votes for each candidate by looping through the counts.
# # 1. Iterate through the candidate list.
# for candidate_name in candidate_votes:
#     # 2. Retrieve vote count of a candidate.
#     votes = candidate_votes[candidate_name]
#     # 3. Calculate the percentage of votes.
#     vote_percentage = float(votes) / float(total_votes) * 100
#     # 4. Print the candidate name and percentage of votes.
#     print(f"{candidate_name}: received {vote_percentage}% of the vote.")
