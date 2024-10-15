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
                if datetime.strptime(exp_date, '%Y-%m-%d').date() < date.today():
                    print("Expiration date cannot be in the past")
                else:
                    break
            except:
                
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
        print("Invalid input. Please try again.")
        
# Appending the published content to a file named "Newsfeed"
try:
    with open("Newsfeed.txt", "a", encoding="utf-8") as file:
        file.write(newsfeed.publish())
        file.write("\n\n")
except: 
    pass
