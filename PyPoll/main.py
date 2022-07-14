# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define vars
candidates = []
votes_per_candidate = []

# Define the path to Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    # Process each row of data after the header
    for row in csv_reader:
        candidates.append(row[2])
    # Sort the data in ascending order
    sorted_list = sorted(candidates)

    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    # Count votes and append to list
    count_candidate = Counter(arrange_list)
    votes_per_candidate.append(count_candidate.most_common())

# calculate the percentage of votes per candicate in 3 digital points
for item in votes_per_candidate:
    first = format((item[0][1]) * 100 / (sum(count_candidate.values())), '.3f')
    second = format((item[1][1]) * 100 / (sum(count_candidate.values())), '.3f')
    third = format((item[2][1]) * 100 / (sum(count_candidate.values())), '.3f')

# Output the data to the terminal
print("Election Results")
print("--------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("----------------------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print("----------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")

# Check if Analysis folder has already been created
isExist = os.path.exists("Analysis")

if not isExist:
    # Create a new directory because it does not exist
    os.mkdir("Analysis")


# Output the data to file
election_data = os.path.join("analysis", "election_data.txt")
with open(election_data, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("--------------------\n")
    outfile.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    outfile.write("----------------------------------------\n")
    outfile.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    outfile.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    outfile.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    outfile.write("----------------------\n")
    outfile.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")