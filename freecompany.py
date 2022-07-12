import requests, re
from bs4  import BeautifulSoup
import datetime

# The base url to the Free Company page on Lodestone
url = "https://eu.finalfantasyxiv.com/lodestone/freecompany/"

# ID for the Free Company we want to scrape/parse
id = "9279667032196907056"

# Grabs html code from Lodestone

result = requests.get(url+id)

doc = BeautifulSoup(result.text, "html.parser")
lst2 = doc.find_all("p", {"class": "freecompany__text__name"}) 

l = str(lst2)
fcName = re.findall(r"(?<=>)[^<]+",l)

timestamp = fcName[9]
formed = re.findall(r"\b\d+\b", timestamp)
for formed in formed:
    formedDate = formed

    formedDate = int(formedDate)

class fc_lodestone_data():

    formed_date = datetime.datetime.fromtimestamp(formedDate) # FC Formed At
    name = fcName[0] # FC Name
    tag = fcName[2] # FC Tag
    fc_formed = f"{formed_date:%Y-%m-%d}" # Convert to readable date