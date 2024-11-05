import sys
import os
from from_txt import FromTXT
from from_json import FromJSON
from from_xml import FromXML
from newsfeed import News, PrivateAd, WhatsTheScore
from task_7 import to_csv
from export_to_db import ToDB


db_connection = ToDB('newsfeed_db.db') # initialize ToDB
db_connection.create_tables() # create tables

# function to write newsfeed items to txt file, DB and recalculate csv statistics
def write_to_file(newsfeed_items):
    try:
        # Open the Newsfeed.txt file in append mode
        with open("Newsfeed.txt", "a", encoding="utf-8") as output:
            # Write each newsfeed item to the file
            for item in newsfeed_items:
                output.write(item.publish())
                output.write("\n\n")
                # Insert records into specific tables in the database
                if isinstance(item, News):
                    db_connection.insert_news(item.text, item.city, item.date)
                elif isinstance(item, PrivateAd):
                    db_connection.insert_private_ad(item.text, item.exp_date, item.days_left)
                elif isinstance(item, WhatsTheScore):
                    db_connection.insert_score(item.team1, item.score, item.team2)

        # Call the to_csv function to update CSV files with new statistics
        to_csv()

    except Exception as e:
        # Print an error message if something goes wrong
        print(f'Error: {e}')

# File paths with defaults if not provided
txt_file_path = sys.argv[1] if len(sys.argv) > 1 else "./txt_input.txt"
json_file_path = sys.argv[2] if len(sys.argv) > 2 else "./json_input.json"
xml_file_path = sys.argv[3] if len(sys.argv) > 3 else "./xml_input.xml"

# Main loop to handle user input
while True:
    start = input("Hello there! What would you like to publish today? Type 1 for JSON, 2 for TXT, 3 for XML, 9 for manual input, 0 to exit: ")
    
    # Exit the program
    if start == "0":
        print("OK, bye")
        break

    # Handle JSON input
    elif start == "1":
        if os.path.exists(json_file_path):
            json_input = FromJSON(json_file_path)
            newsfeed_items = json_input.process_json(News, PrivateAd, WhatsTheScore)
            write_to_file(newsfeed_items)
        else:
            print('No file here')

    # Handle txt input
    elif start == "2":
        if os.path.exists(txt_file_path):
            txt_input = FromTXT(txt_file_path)
            newsfeed_items = txt_input.process_txt(News, PrivateAd, WhatsTheScore)
            write_to_file(newsfeed_items)
        else:
            print('No file here')

    elif start == "3":
        if os.path.exists(xml_file_path):
            xml_input = FromXML(xml_file_path)
            newsfeed_items = xml_input.process_xml(News, PrivateAd, WhatsTheScore)
            write_to_file(newsfeed_items)

    # Manual input
    elif start == "9":
        # User input to choose the type of content to publish
        type = input("What would you like to publish? Type 1 for News, 2 for Private Ad, 3 for Score or 0 to exit: ")

        if type == "1":
            text = input("Input the story that you'd like to publish: ")
            city = input("Input in what city did the story happen: ")
            newsfeed_items = News(text, city)
            write_to_file([newsfeed_items])

        elif type == "2":
            text = input("Input the ad that you'd like to publish: ")
            exp_date = input("Input the expiration date in format YYYY-MM-DD: ")
            newsfeed_items = PrivateAd(text, exp_date)
            write_to_file([newsfeed_items])

        elif type == "3":
            team1 = input("Input home side: ")
            team2 = input("Input away side: ")
            newsfeed_items = WhatsTheScore(team1, team2)
            write_to_file([newsfeed_items])

        else:
            # error handling for invalid input
            print("Invalid input. Please try again.")
            
    else:
        # error handling for invalid input
        print("Invalid input. Please try again.")
