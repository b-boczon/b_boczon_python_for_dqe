from datetime import date, datetime
from random import randint

# Base class for publishing 
class Newsfeed:
    def __init__(self, text):
        self.text = text

    def publish(self):
        return f"{self.text}"

# Class with inheritance for publishing news for given city and current datetime
class News(Newsfeed):
    def __init__(self, text, city):
        super().__init__(text)  # Call to the superclass to store the text
        self.city = city  # Additional attribute for city
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M')  # Stores current datetime in string format

    # Publishing format for News
    def publish(self):
        return f"News ------------\n{self.text}\n{self.city}, {self.date}"

# Class with inheritance for publishing private ads which include an expiration date and calculate days left
class PrivateAd(Newsfeed):
    def __init__(self, text, exp_date):
        super().__init__(text)  # Call to the superclass to store the text
        self.exp_date = datetime.strptime(exp_date, '%Y-%m-%d').date()  # Converts string to a date
        self.days_left = (self.exp_date - date.today()).days  # Calculates days left until expiration

    # Publishing format for Private Ad
    def publish(self):
        return f"Private Ad ------\n{self.text}\nActual until: {self.exp_date}, {self.days_left} days left"

# Class for generating a score between two teams
class WhatsTheScore:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    # Publishing format for Scores
    def publish(self):
        # Generates random scores for each team
        return f"Todays score ---- \n{self.team1} {randint(0,3)} : {randint(0,3)} {self.team2} \nGo sports!"

# User input to choose the type of content to publish
type = input("Would you like to publish? Type news, private ad or score. ")

if type == 'news':
    text = input("Input the story that you'd like to publish: ")
    city = input("Input in what city did the story happen: ")
    newsfeed = News(text, city)
elif type == 'private ad':
    text = input("Input the ad that you'd like to publish: ")
    exp_date = input("Input the expiration date in format YYYY-MM-DD: ")

    # Error handling for past dates
    if datetime.strptime(exp_date, '%Y-%m-%d').date() < date.today():
        raise ValueError("Expiration date cannot be in the past")
    
    newsfeed = PrivateAd(text, exp_date)
elif type == 'score':
    team1 = input("Input home side: ")
    team2 = input("Input away side: ")
    newsfeed = WhatsTheScore(team1, team2)
else:
    print('No such thing, try again later')  # Error message if the input doesn't match any specified type

# Appending the published content to a file named "Newsfeed"
with open("Newsfeed", "a") as file:
    file.write(newsfeed.publish())
    file.write("\n\n")
