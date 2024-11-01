import os

# Class for processing newsfeed from file
class FromTXT:
    def __init__(self, file_path):
        self.file_path = file_path

    # Method to process the TXT file and create newsfeed items for publishing
    def process_txt(self, News, PrivateAd, WhatsTheScore):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                text = file.read().lower().splitlines() # read text in lower case to avoid missed records, text formatting moved to class

                newsfeed_items = [] # List to hold the created newsfeed items
                for i in range(0, len(text), 3):
                    news_type = text[i].strip() # parts of newsfeed are separated by new line
                    part1 = text[i+1].strip()
                    part2 = text[i+2].strip()
                    if news_type == "news":
                        newsfeed_items.append(News(part1, part2))
                    elif news_type == "private ad":
                        newsfeed_items.append(PrivateAd(part1, part2))
                    elif news_type == "score":
                        newsfeed_items.append(WhatsTheScore(part1, part2))
                    
            os.remove(self.file_path) # remove file after processing succesfuly

            print("File processed succesfuly")
        except Exception as e:
            print(f"error {e}") # error handling

        return newsfeed_items    # Return the list of newsfeed items
 