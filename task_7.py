import regex
import csv
from collections import Counter

# function to calculate statistics and place it in csv file
def to_csv():
    with open("Newsfeed.txt", "r", encoding = "utf-8") as file:
        text = file.read()
    # Use regex to find all words
    words = regex.findall(r'\p{L}+', text.lower())
    # Find all letters in the text
    all_letters = regex.findall(r'\p{L}', text)
    # Find all uppercase letters in the  text
    uppercase_letters = regex.findall(r'\p{Lu}', text)

    # Count occurrences of each word and letter and sum of all letters
    dict_of_words = dict(Counter(words))
    dict_of_letters = dict(Counter(all_letters))
    dict_of_uppercase = dict(Counter(uppercase_letters))
    count_of_all_letters = sum(dict_of_letters.values())

    # Write the word counts to a csv file from dict
    with open("word_count.csv", "w", newline="", encoding="utf-8") as f1:
        w = csv.writer(f1)
        # write the dict items to csv file row by row
        for wrd, cnt in dict_of_words.items():
            w.writerow([wrd, cnt])

    csv_input = []
    # Loop through all letters
    for letter, cnt_let in dict_of_letters.items():
        # Get count of uppercase 
        cnt_upper = dict_of_uppercase.get(letter, 0)
        # each letter out of all letters
        percentage_of_all = (cnt_let/count_of_all_letters) * 100
        # count each upper letter out of all letters
        percentage_of_all_upper = (cnt_upper/count_of_all_letters) * 100
        # Append the letter data to the list for csv output
        csv_input.append([letter, cnt_let, round(percentage_of_all, 2), round(percentage_of_all_upper, 2)])

    # Write the letter data to another csv file
    with open("letter_count.csv", "w", newline="", encoding="utf-8") as f2:
        # define headers
        headers = ("letter", "count_all", "percentage_of_all", "percentage_of_all_upper")
        l = csv.writer(f2)
        # write headers to csv file
        l.writerow(headers)
        # write the rest to csv file row by row
        for row in csv_input:
            l.writerow(row)
