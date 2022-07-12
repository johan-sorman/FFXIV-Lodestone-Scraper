import requests, re
from bs4  import BeautifulSoup
import datetime

# The base url to the Free Company page on Lodestone
url = "https://eu.finalfantasyxiv.com/lodestone/freecompany/"

# ID for the Free Company we want to scape
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

    formed_date = datetime.datetime.fromtimestamp(formedDate)
    name = fcName[0]
    tag = fcName[2]
    fc_formed = f"{formed_date:%Y-%m-%d}"