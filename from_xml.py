import xml.etree.ElementTree as ET
import os

class FromXML:
    def __init__(self, file_path):
        self.file_path = file_path

    def process_xml(self, News, PrivateAd, WhatsTheScore):

        xml_file = ET.parse(self.file_path)
        root = xml_file.getroot()
        newsfeed_items = []

        try:
            for item in root.findall("type"):
                news_type = item.get("news_type").lower()
                txt = item.find("text").text if item.find('text') is not None else ""
                cit = item.find("city").text if item.find("city") is not None else ""
                exp = item.find("exp_date").text if item.find("exp_date") is not None else ""
                t1 = item.find("team1").text if item.find("team1") is not None else ""
                t2 = item.find("team2").text if item.find("team2") is not None else ""

                if news_type == "news":
                    newsfeed_items.append(News(txt,cit))
                elif news_type == "private ad":
                    newsfeed_items.append(PrivateAd(txt, exp))
                elif news_type == "score":
                    newsfeed_items.append(WhatsTheScore(t1, t2))
            
            os.remove(self.file_path) # remove file after processing succesfuly
            print("File processed succesfuly")

        except Exception as e:
            print(f"Error: {e}")
        return newsfeed_items    # Return the list of newsfeed items
 

# ET.dump(root) # printout for debugging
