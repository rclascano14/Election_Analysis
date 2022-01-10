# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who receieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attributre on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is", now)
# The time right now is 2022-01-07 16:00:06.721914
import csv
import os
# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file. 
with open(file_to_load) as election_data:

# Print the file object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    txt_file.write("Hellow World")
# Write three counties to the file.
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")
