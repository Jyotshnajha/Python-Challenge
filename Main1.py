import os
import csv
import statistics

election_data = os.path.join("..","PyRoll","Resources","election_data.csv")

election_analysis = os.path.join("..","PyRoll", "Resources","election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(election_data, encoding ='UTF-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
                        candidate_options.append(candidate_name)
                        candidate_votes[candidate_name] = 0
                        candidate_votes[candidate_name] += 1


with open(election_analysis, "w") as txt_file:
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    
    txt_file.write(election_results)
    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

   
        print(candidate_results)
        
        txt_file.write(candidate_results)
       
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
   
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)


