import os
import csv

# Defining the variables
votes = []
county = []
candidates = []
Correy = []
Khan = []
Li = []
Otooley = []

#Define path
main_csv = os.path.join( 'Resources', 'election_data.csv')

# Open and read csv
with open(main_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

        # Read header row 
    csv_header = next(csv_file)

    #print(f"header: {csv_header}")

    #Read through rows
    for row in csv_reader:

        # For votes, add to votes, county, candidates
        votes.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

        # Calculating total votes casted
        total_votes = (len(votes))
        #print(total_votes)

    # A complete list of candidates who received votes
    for candidate in candidates:
        if candidate == "Correy":
           Correy.append(candidates)
           Correy_votes = len(Correy)
        
        elif candidate == "Khan":
            Khan.append(candidates)
            Khan_votes = len(Khan)

        elif candidate == "Li":
            Li.append(candidates)
            Li_votes = len(Li)

        else:
            Otooley.append(candidates)
            Otooley_votes = len(Otooley)

    #Print votes by candidate
    #print(Correy_votes)
    #print(Khan_votes)
    #print(Li_votes)
    #print(Otooley_votes)

    #   The percentage of votes each candidate won
    Correy_percent = round(((Correy_votes/total_votes) * 100), 2)
    Khan_percent = round(((Khan_votes/total_votes) * 100), 2)
    Li_percent = round(((Li_votes/total_votes) * 100), 2)
    Otooley_percent = round(((Otooley_votes/total_votes) * 100), 2)
    
    # Print percentage of votes each candidate won
    #print(Correy_percent)
    #print(Khan_percent)
    #print(Li_percent)
    #print(Otooley_percent)

    # The winner of the election based on popular vote.
    if Correy_votes > max(Khan_percent, Li_percent, Otooley_percent):
        winner = "Correy"
    elif Khan_percent > max(Correy_percent, Li_percent, Otooley_percent):
        winner = "Khan"
    elif Li_percent > max(Correy_percent, Khan_percent, Otooley_percent):
        winner = "Li"
    else:
        winner = "Otooley"

''' Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
''' 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Correy: {Correy_percent}% ({Correy_votes})")
print(f"Khan: {Khan_percent}% ({Khan_votes})")
print(f"Li: {Li_percent}% ({Li_votes})")
print(f"Otooley: {Otooley_percent}% ({Otooley_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
PyPoll_file = os.path.join("Resources", "PyPoll_JBK.txt")
with open (PyPoll_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes {total_votes}\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Correy: {Correy_percent}% ({Correy_votes}\n")
    outfile.write(f"Khan: {Khan_percent}% ({Khan_votes}\n")
    outfile.write(f"Li: {Li_percent}% ({Li_votes}\n")
    outfile.write(f"Otooley: {Otooley_percent}% ({Otooley_votes}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")







'''------------------------------------------------------------------------------------------------------------------------------
Disregard everything from here. My answer is different from answer provided. I tried figuring it out. i ran out of time. JB Kinlacheeny

[Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town 
modernize its vote counting process.

* You will be give a set of poll data called 
[eslection_data.csv](PyPoll/Resources/election_data.csv). 
Te dataset is composed of three columns: 
`Voter ID`, `County`, and `Candidate`. 
Your task is to create a Python script that analyzes the votes and 
calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''
