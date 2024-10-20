import re
import csv
from collections import Counter

with open("Newsfeed.txt", "r", encoding = "utf-8") as file:
    text = file.read()
# Use regex to find all words
words = re.findall(r"[a-zA-Z']+", text.lower())
# Find all letters in the text
all_letters = re.findall(r'[a-zA-Z]', text.upper())
# Find all uppercase letters in the  text
uppercase_letters = re.findall(r'[A-Z]', text)

# Count occurrences of each word and letter
dict_of_words = dict(Counter(words))
dict_of_letters = dict(Counter(all_letters))
dict_of_uppercase = dict(Counter(uppercase_letters))

# Write the word counts to a csv file from dict
with open("word_count.csv", "w", newline="", encoding="utf-8") as f1:
    w = csv.writer(f1)
    # write the dict items to csv file row by row
    for wrd, cnt in dict_of_words.items():
        w.writerow([wrd, cnt])

csv_input = []
# Loop through all letters
for letter, cnt_all in dict_of_letters.items():
    # Get count of uppercase 
    cnt_upper = dict_of_uppercase.get(letter, 0)
    # Calculate the percentage of uppercase in all letters
    percentage_of_uppercase = (cnt_upper / cnt_all) * 100  if cnt_all > 0 else 0
    # Append the letter data to the list for csv output
    csv_input.append([letter, cnt_all, cnt_upper, percentage_of_uppercase])

# Write the letter data to another csv file
with open("letter_count.csv", "w", newline="", encoding="utf-8") as f2:
    # define headers
    headers = ("letter", "count_all", "count_uppercase", "percentage")
    l = csv.writer(f2)
    # write headers to csv file
    l.writerow(headers)
    # write the rest to csv file row by row
    for row in csv_input:
        l.writerow(row)
