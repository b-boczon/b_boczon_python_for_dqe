import os
import sys
# import functions from task 4_3 to normalize case
from task4_3 import split_paragraphs, split_sentences, normalize_case, build_final_text
from datetime import date, datetime
from random import randint

# Base class for publishing 
class Newsfeed:
    def __init__(self, text):
        self.text = text

    def publish(self):
        return self.text
    
    def header(self, head):
        return f"{head} ------------\n"

# Class with inheritance for publishing news for given city and current datetime
class News(Newsfeed):
    def __init__(self, text, city):
        super().__init__(text)  # Call to the superclass to store the text
        self.city = city  # Additional attribute for city
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M')  # Stores current datetime in string format

    # Publishing format for News
    def publish(self):
        head = self.header("News")
        return f"{head}{self.text}\n{self.city}, {self.date}"

# Class with inheritance for publishing private ads which include an expiration date and calculate days left
class PrivateAd(Newsfeed):
    def __init__(self, text, exp_date):
        super().__init__(text)  # Call to the superclass to store the text
        self.exp_date = datetime.strptime(exp_date, '%Y-%m-%d').date()  # Converts string to a date
        self.days_left = (self.exp_date - date.today()).days  # Calculates days left until expiration

    # Publishing format for Private Ad
    def publish(self):
        head = self.header("Private Ad")
        return f"{head}{self.text}\nActual until: {self.exp_date}, {self.days_left} days left"

# Class for generating a score between two teams
class WhatsTheScore(Newsfeed):
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    # Publishing format for Scores
    def publish(self):
        head = self.header("Todays score")
        # Generates random scores for each team
        return f"{head}{self.team1} {randint(0,3)} : {randint(0,3)} {self.team2} \nGo sports!"

# Class for processing newsfeed from file
class FromFile:
    def __init__(self, file_path):
        self.file_path = file_path

    # Class for processing newsfeed from file
    def process_file(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as input:
                text = input.read()             # read file
                par = split_paragraphs(text)    # use functions form task 4_3 to normalize case
                sent = split_sentences(par)
                norm = normalize_case(sent)
                txt = build_final_text(norm).splitlines() # build final text and split by new line for processing
                for i in range(0, len(txt), 3):
                    news_type = txt[i].strip() # parts of newsfeed are separated by new line
                    part1 = txt[i+1].strip()
                    part2 = txt[i+2].strip()
                    if news_type == "News":
                        newsfeed = News(part1, part2)
                    elif news_type == "Private ad":
                        newsfeed = PrivateAd(part1, part2)
                    elif news_type == "Score":
                        newsfeed = WhatsTheScore(part1, part2)
                    
                    with open("Newsfeed.txt", "a", encoding="utf-8") as file:
                        file.write(newsfeed.publish())
                        file.write("\n\n")
                
            os.remove(self.file_path) # remove file after processing succesfuly

            print("File processed succesfuly")
        except Exception as e:
            print(f"error {e}") # error handling

file_path = sys.argv[1] if len(sys.argv) > 1 else "./input.txt" # create variable foe file path

# if file input.txt exists then proceed with input from file, if not, go to manula input
if os.path.exists(file_path):
    file_processor = FromFile(file_path)
    file_processor.process_file()
else:
    # Create continious menu using while loop to avoid getting errors with wrong input:
    while True:
        # User input to choose the type of content to publish
        type = input("What would you like to publish? Type 1 for News, 2 for Private Ad, 3 for Score or 0 to exit: ")

        if type == "1":
            text = input("Input the story that you'd like to publish: ")
            city = input("Input in what city did the story happen: ")
            newsfeed = News(text, city)
            break
        elif type == "2":
            text = input("Input the ad that you'd like to publish: ")
            while True:
                exp_date = input("Input the expiration date in format YYYY-MM-DD: ")
                try:
                    # error handling for past date
                    if datetime.strptime(exp_date, '%Y-%m-%d').date() < date.today():
                        print("Expiration date cannot be in the past")
                    else:
                        break
                except:
                    # error handling for invalid format
                    print("Invalid date format. Please try again.")      
            newsfeed = PrivateAd(text, exp_date)
            break
        elif type == "3":
            team1 = input("Input home side: ")
            team2 = input("Input away side: ")
            newsfeed = WhatsTheScore(team1, team2)
            break
        elif type == "0":
            print("OK, bye")
            break
        
        else:
            # error handling for invalid input
            print("Invalid input. Please try again.")
            
# Appending the published content to a file named "Newsfeed.txt"
try:
    with open("Newsfeed.txt", "a", encoding="utf-8") as file:
        file.write(newsfeed.publish())
        file.write("\n\n")
except: 
    # If no input - do nothing
    pass
