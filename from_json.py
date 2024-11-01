import json
import os

# Class for processing input from JSON file
class FromJSON:
    def __init__(self, file_path):
        self.file_path = file_path

    # Method to process the JSON file and create newsfeed items for publishing
    def process_json(self, News, PrivateAd, WhatsTheScore):
        try:
            with open(self.file_path, "r") as file: # Open and read the JSON file
                json_input = json.load(file) # Load the JSON data into a dictionary

            newsfeed_items = [] # List to hold the created newsfeed items
            # Extract data for each type of newsfeed item
            for v in json_input.values():
                news_type = v.get("news_type", "").lower() # read text in lower case to avoid missed records, text formatting moved to class
                text = v.get("text", "").lower()
                city = v.get("city", "").lower()
                exp_date = v.get("exp_date", "").lower()
                team1 = v.get("team1", "").lower()
                team2 = v.get("team2", "").lower()
                news_type = v.get("news_type").lower()

                # Create the appropriate newsfeed item based on the type and add it to the list
                if news_type == "news":
                    newsfeed_items.append(News(text, city))
                elif news_type == "private ad":
                    newsfeed_items.append(PrivateAd(text, exp_date))
                elif news_type == "score":
                    newsfeed_items.append(WhatsTheScore(team1, team2))

            # Remove the JSON file after processing to avoid reprocessing the same data
            os.remove(self.file_path)
            print("File processed successfully and deleted")
        except Exception as e:
            print(f"Error: {e}")
        return newsfeed_items    # Return the list of newsfeed items
 