import requests, re
from bs4  import BeautifulSoup
import datetime

        # The base url to the Free Company page on Lodestone
        
url = "https://eu.finalfantasyxiv.com/lodestone/freecompany/"

        # ID for the Free Company we want to scape
        
id = "9279667032196907056"

        # Grabs html code from Lodestone

result = requests.get(url+id)

lodestone_page = BeautifulSoup(result.text, "html.parser")

        # Contains data for Member Count and Current Rank

lst = lodestone_page.find_all("p", {"class": "freecompany__text"}) 

        # Contains data for Name, Tag & Formed Date
lst2 = lodestone_page.find_all("p", {"class": "freecompany__text__name"}) 

for Rank in lst[4]:
    fcRank = Rank
for Members in lst[3]:
    activeMembers = Members
LStr = str(lst2)
fcName = re.findall(r"(?<=>)[^<]+",LStr)

timestamp = fcName[9]
formed = re.findall(r"\b\d+\b", timestamp)
for formed in formed:
    formedDate = formed
    formedDate = int(formedDate) # Convert to INT in order for datetime function to do it's thing

        # Class so functions can be called outside of this script

class fc_lodestone_data():
    formed_date = datetime.datetime.fromtimestamp(formedDate)
    name = fcName[0]
    tag = fcName[2]
    fc_formed = f"{formed_date:%Y-%m-%d}"
    fcRank = Rank
    activeMembers = Members