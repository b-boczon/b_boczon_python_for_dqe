from datetime import datetime, date
from random import randint
import sys
from task4_3 import split_sentences, normalize_case, build_final_text

# function to normalize case to keep the code DRY
def normalize(txt):
    split_txt = split_sentences(txt)
    normalized_text = normalize_case(split_txt)
    final_text = build_final_text(normalized_text)

    return final_text

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

    # Publishing format for News. Text formatting was moved here to keep the code DRY
    def publish(self):
        head = self.header("News")
        txt = normalize([self.text])
        cit = normalize([self.city])
        return f"{head}{txt}\n{cit}, {self.date}"

# Class with inheritance for publishing private ads which include an expiration date and calculate days left
class PrivateAd(Newsfeed):
    def __init__(self, text, exp_date):
        super().__init__(text)  # Call to the superclass to store the text
        
        # Check if the date is not in the past was moved here to keep the code DRY
        try:
            exp = datetime.strptime(exp_date, '%Y-%m-%d').date()  # Converts string to a date
            if exp < date.today():
                raise ValueError("Expiration date cannot be in the past")
        except ValueError as e:
            print(e)
            sys.exit() # If date is in the past program quits. TODO - introduce good and bad record parser

        self.exp_date = exp
        self.days_left = (self.exp_date - date.today()).days # Calculates days left until expiration

    # Publishing format for Private Ad. Text formatting was moved here to keep the code DRY
    def publish(self):
        head = self.header("Private Ad")
        txt = normalize([self.text])
        return f"{head}{txt}\nActual until: {self.exp_date}, {self.days_left} days left"

    # Class for generating a score between two teams
class WhatsTheScore(Newsfeed):
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    # Publishing format for Scores. Text formatting was moved here to keep the code DRY
    def publish(self):
        head = self.header("Todays score")
        t1 = normalize([self.team1])
        t2 = normalize([self.team2])
        self.score = f"{randint(0,3)} : {randint(0,3)}" # Generates random scores for each team
        return f"{head}{t1} {self.score} {t2} \nGo sports!"
