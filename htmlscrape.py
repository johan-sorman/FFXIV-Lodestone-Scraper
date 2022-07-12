import requests, json
import base64
from bs4  import BeautifulSoup

# The base url to the Free Company page on Lodestone
url = "https://eu.finalfantasyxiv.com/lodestone/freecompany/"

# ID for the Free Company we want to scape
id = str(9279667032196907056)

# Grabs html code from Lodestone
result = requests.get(url+id)

