from multiprocessing.dummy import active_children
from threading import activeCount
import requests, json
import base64
import re
from bs4  import BeautifulSoup

# The base url to the Free Company page on Lodestone
url = "https://eu.finalfantasyxiv.com/lodestone/freecompany/"

# ID for the Free Company we want to scape
id = "9279667032196907056"

# Grabs html code from Lodestone

result = requests.get(url+id)

doc = BeautifulSoup(result.text, "html.parser")
lst = doc.find_all("p", {"class": "freecompany__text"}) 
for Rank in lst[4]:
    print(Rank)